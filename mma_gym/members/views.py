from django.http import JsonResponse
from .services.google_sheets import get_all_members, add_member, update_member, delete_member

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
