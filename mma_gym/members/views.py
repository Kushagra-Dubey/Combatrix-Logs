import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .services.google_sheets import Member, Membership
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .utils import clean_phone


class MemberView(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.member = Member()

    def get(self, request, *args, **kwargs):
        """Handle GET requests, fetch members data."""
        members = self.member.get_all_members()  # Fetch members' data from Google Sheets
        # Massage the data by renaming keys to remove spaces and simplify
        for member in members:
            member["Date_of_Birth"] = member.pop("Date of Birth ")
            member["Emergency_Contact_Name"] = member.pop(
                "Emergency Contact Name ")
            member["Emergency_Contact_Number"] = clean_phone(
                member.pop("Phone number"))
            member['Consent_To_Media'] = member.pop(
                'I consent to Combatrix Academy using photographs or videos of me during training sessions for promotional or educational purposes.')
            member['Agreement_To_Terms'] = member.pop(
                'I have read, understand, and agree to the terms outlined in this waiver and release of liability.')
        return render(request, 'members/members_table.html', {'members': members})

    def post(self, request, *args, **kwargs):
        """Handle POST requests for adding, updating, and deleting members."""
        action = request.POST.get('action')  # Get the action from POST data

        if action == 'add':
            return self.add_member_view(request)
        elif action == 'update':
            return self.update_member_view(request)
        elif action == 'delete':
            return self.delete_member_view(request)

        return JsonResponse({"error": "Invalid request"}, status=400)

    def add_member_view(self, request):
        """Add a new member."""
        data = request.POST.getlist(
            "data")  # Example: ["Name", "Plan", "Start Date"]
        self.member.add_member(data)
        return JsonResponse({"message": "Member added successfully"})

    def update_member_view(self, request):
        """Update member information."""
        row = int(request.POST["row"])
        column = int(request.POST["column"])
        value = request.POST["value"]
        self.member.update_member(row, column, value)
        return JsonResponse({"message": "Member updated successfully"})

    def delete_member_view(self, request):
        """Delete a member."""
        row = int(request.POST["row"])
        self.member.delete_member(row)
        return JsonResponse({"message": "Member deleted successfully"})


class MembershipView(View):
    def __init__(self):
        self.membership = Membership()

    def list_memberships(self, request):
        """Render the memberships page."""
        memberships = self.membership.get_all_memberships()
        print("memberships", memberships)
        return render(request, "memberships/memberships_table.html", {"memberships": memberships})

    @method_decorator(csrf_exempt)
    def add_membership(self, request):
        """Handle adding a new membership."""
        if request.method == "POST":
            try:
                data = json.loads(request.body)
                plan_name = data.get("plan_name")
                plan_duration = data.get("plan_duration")
                price = data.get("price")
                if not all([plan_name, plan_duration, price]):
                    return JsonResponse({"error": "Invalid data"}, status=400)
                self.membership.add_membership([plan_name, plan_duration, price])
                return JsonResponse({"message": "Membership added successfully"})
            except json.JSONDecodeError:
                return JsonResponse({"error": "Invalid JSON"}, status=400)
        return JsonResponse({"error": "Invalid request"}, status=400)