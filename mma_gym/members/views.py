from django.http import JsonResponse
from django.shortcuts import render
from .services.google_sheets import get_all_members, add_member, update_member, delete_member
from .utils import clean_phone

def list_members(request):
    """Fetch and return all members."""
    data = get_all_members()
    return JsonResponse({"members": data})

def add_member_view(request):
    """Add a new member."""
    if request.method == "POST":
        data = request.POST.getlist("data")  # Example: ["Name", "Plan", "Start Date"]
        add_member(data)
        return JsonResponse({"message": "Member added successfully"})
    return JsonResponse({"error": "Invalid request"}, status=400)

def update_member_view(request):
    """Update member information."""
    if request.method == "POST":
        row = int(request.POST["row"])
        column = int(request.POST["column"])
        value = request.POST["value"]
        update_member(row, column, value)
        return JsonResponse({"message": "Member updated successfully"})
    return JsonResponse({"error": "Invalid request"}, status=400)

def delete_member_view(request):
    """Delete a member."""
    if request.method == "POST":
        row = int(request.POST["row"])
        delete_member(row)
        return JsonResponse({"message": "Member deleted successfully"})
    return JsonResponse({"error": "Invalid request"}, status=400)


def members_table(request): 
    members = get_all_members()  # Fetch members' data from Google Sheets
    # Massage the data by renaming keys to remove spaces and simplify
    for member in members:
        member["Date_of_Birth"] = member.pop("Date of Birth ")
        member["Emergency_Contact_Name"] = member.pop("Emergency Contact Name ") 
        member["Emergency_Contact_Number"] = clean_phone(member.pop("Phone number"))
        member['Consent_To_Media'] = member.pop('I consent to Combatrix Academy using photographs or videos of me during training sessions for promotional or educational purposes.')
        member['Agreement_To_Terms'] = member.pop('I have read, understand, and agree to the terms outlined in this waiver and release of liability.')
    print("members", members)
    return render(request, 'members/members_table.html', {'members': members})