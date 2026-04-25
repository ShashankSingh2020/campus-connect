from django.shortcuts import render, get_object_or_404
from .models import JobListing, Application


# This view shows the list of all jobs
def index(request):
    # Check if the user typed something in the search bar
    query = request.GET.get('search')

    if query:
        # Filter jobs where the title contains the search word (case-insensitive)
        jobs = JobListing.objects.filter(title__icontains=query).order_by('-posted_at')
    else:
        # Otherwise, show all jobs
        jobs = JobListing.objects.all().order_by('-posted_at')

    return render(request, 'index.html', {'jobs': jobs, 'query': query})


# This view handles the job application form
def apply(request, pk):
    # Get the specific job using its ID (pk)
    job = get_object_or_404(JobListing, id=pk)

    if request.method == "POST":
        # Get data from the HTML form
        student_name = request.POST.get('name')
        email = request.POST.get('email')
        resume = request.FILES.get('resume')

        # Save to the database
        Application.objects.create(
            job=job,
            student_name=student_name,
            email=email,
            resume=resume
        )
        return render(request, 'success.html', {'job': job})

    return render(request, 'apply.html', {'job': job})