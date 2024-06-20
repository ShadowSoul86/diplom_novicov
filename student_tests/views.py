from django.shortcuts import render, get_object_or_404, redirect
from .models import Test, Question, Answer, TestResult
from .forms import NameForm
from .utils import get_ball_declension


def test_list(request):
    tests = Test.objects.all()
    return render(request, 'student_tests/test_list.html', {'tests': tests})


def start_test(request, test_slug):
    test = get_object_or_404(Test, slug=test_slug)
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            request.session['name'] = name
            first_question = Question.objects.filter(test=test).first()
            if first_question:
                return redirect('question_detail', test_slug=test.slug, question_id=first_question.id)
    else:
        form = NameForm()
    return render(request, 'student_tests/start_test.html', {'test': test, 'form': form})


def question_detail(request, test_slug, question_id):
    question = get_object_or_404(
        Question, id=question_id, test__slug=test_slug)
    test = question.test
    if request.method == 'POST':
        selected_answer_id = request.POST.get(f'question_{question.id}')
        if selected_answer_id:
            selected_answer = get_object_or_404(Answer, id=selected_answer_id)
            if 'answers' not in request.session:
                request.session['answers'] = {}
            request.session['answers'][str(
                question.id)] = selected_answer.is_correct
            request.session.modified = True  # Убедитесь, что сессия будет сохранена
            next_question = Question.objects.filter(
                test=test, id__gt=question.id).first()
            if next_question:
                return redirect('question_detail', test_slug=test.slug, question_id=next_question.id)
            else:
                return redirect('submit_test', test_slug=test.slug)
    return render(request, 'student_tests/question_detail.html', {'question': question})


def submit_test(request, test_slug):
    if request.method == 'POST' or 'answers' in request.session:
        test = get_object_or_404(Test, slug=test_slug)
        answers = request.session.pop('answers', {})
        correct_answers = sum(
            1 for is_correct in answers.values() if is_correct)

        score = correct_answers
        name = request.session.get('name', 'Аноним')
        TestResult.objects.create(test=test, name=name, score=score)
        return redirect('test_result', score=score)
    return redirect('test_list')


def test_result(request, score):
    declension = get_ball_declension(score)
    name = request.session.get('name', 'Аноним')
    return render(request, 'student_tests/test_result.html', {'score': score, 'declension': declension, 'name': name})


def test_results(request):
    results = TestResult.objects.all()
    return render(request, 'student_tests/test_results.html', {'results': results})
