from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse, reverse_lazy
from .models import GolfCourse
from .forms import GolfCourseForm

# Create your views here.

# Class based views


class GolfCourseListView(ListView):
    model = GolfCourse
    template_name = "home/golfcourse_list.html"


class GolfCourseDetailView(DetailView):
    model = GolfCourse
    template_name = "home/golfcourse_detail.html"


class GolfCourseCreateView(CreateView):
    model = GolfCourse
    form_class = GolfCourseForm
    template_name = "home/golfcourse_form.html"
    success_url = reverse_lazy("golfcourse_list")


class GolfCourseUpdateView(UpdateView):
    model = GolfCourse
    form_class = GolfCourseForm
    template_name = "home/golfcourse_form.html"
    success_url = reverse_lazy("golfcourse_list")


class GolfCourseDeleteView(DeleteView):
    model = GolfCourse
    template_name = "home/golfcourse_confirm_delete.html"


def golf_courses_list(request):
    courses = GolfCourse.objects.all()
    return render(
        request,
        'home/golf_course_display.html',
        {'courses': courses}
    )


def post_view(request):
    post_id = 1
    url = reverse('post_detail', args=[post_id])
    return redirect(url)


def home_view(request):
    return render(request, "base.html")


def delete_golfcourse(request, course_id):
    course = get_object_or_404(GolfCourse, id=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Golf course successfully deleted.')
        return redirect('golfcourse_list')
