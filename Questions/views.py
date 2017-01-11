
from django.shortcuts import render, redirect
from .models import User, Question

# Create your views here.
ALL_Questions = Question.objects.all()

Question1 = ALL_Questions.get(id=1)
Question2 = ALL_Questions.get(id=2)
Question3 = ALL_Questions.get(id=3)
Question4 = ALL_Questions.get(id=4)
Question5 = ALL_Questions.get(id=5)
Question6 = ALL_Questions.get(id=6)
Question7 = ALL_Questions.get(id=7)
Question8 = ALL_Questions.get(id=8)
Question9 = ALL_Questions.get(id=9)
Question10 = ALL_Questions.get(id=10)

context = {
    "questions": ALL_Questions,
    "Question1": Question1,
    "Question2": Question2,
    "Question3": Question3,
    "Question4": Question4,
    "Question5": Question5,
    "Question6": Question6,
    "Question7": Question7,
    "Question8": Question8,
    "Question9": Question9,
    "Question10": Question10,
}

def LoginPage(request):

    UserDB = User.objects.all()

    global login
    login = request.POST.get("Login")
    password = request.POST.get("Password")

    if request.method == 'POST':
        FindLogin = UserDB.filter(Login=login)

        if FindLogin == FindLogin:

            for entry in FindLogin:
                if entry.Password == password:

                    context["login"] = login

                    return redirect(QuestionsPage )

                else:

                    context["error"] = "Password incorrect. Please try again."
                    return render(request, 'LoginPage.html', context)
            else:

                context["error"] = "Login incorrect. Please try again."
                return render(request, 'LoginPage.html', context)

    return render(request, 'LoginPage.html', context)

def RegisterPage(request):

    if request.method == 'POST':
        if request.POST.get("FirstName") != None:

            FirstName = request.POST.get("FirstName")
            LastName = request.POST.get("LastName")
            Login = request.POST.get("Login")
            Password = request.POST.get("Password")

            new_user = User(FirstName=FirstName, LastName=LastName, Login=Login, Password=Password)
            new_user.save()

            context = {"Message": "Account successfully created."}

            return render(request, "RegisterPage.html", context)

    else:

        context = {"Message": "Please fill all fields."}
        return render(request, "RegisterPage.html", context)

def QuestionsPage(request):

    global TotalScores
    TotalScores = 0

    if request.method == "POST":

        if request.POST.get("Q1") == "Галактика":
            TotalScores += 10
        if request.POST.get("Q2") == "Никак":
            TotalScores += 10
        if request.POST.get("Q3") == "Простейший, одноклеточный организм":
            TotalScores += 10
        if request.POST.get("Q4") == "3-й":
            TotalScores += 10
        if request.POST.get("Q5") == "Левай Страусс":
            TotalScores += 10
        if request.POST.get("Q6") == "Москва слезам не верит":
            TotalScores += 10
        if request.POST.get("Q7") == "Гончаров - 'Обломов'":
            TotalScores += 10
        if request.POST.get("Q8") == "Бетховен":
            TotalScores += 10
        if request.POST.get("Q9") == "Франклину":
            TotalScores += 10
        if request.POST.get("Q10") == "Чарльз Бэббидж":
            TotalScores += 10

        FindUser = User.objects.get(Login=login)

        FindUser.TotalScores = TotalScores
        FindUser.save()

        return redirect(ResultPage)

    else:
        return render(request, "QuestionsPage.html", context)

def ResultPage(request):
    context["login"] = login
    context["TotalScores"] = TotalScores

    return render(request, "ResultPage.html", context )