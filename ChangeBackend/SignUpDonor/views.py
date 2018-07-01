from django.shortcuts import render
from .models import User, Password, PersonalDetails, CCDetails, RoundUpDetails
# from .forms import PostForm


def post_new(request):
    # if request.method == "POST":
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         f = form.save(commit=False)
    #         f.save()
    #
    # else:
    #     form = PostForm()

    return render(request, 'SignUpDonor/Donor.html', {})

