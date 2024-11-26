from django.shortcuts import render, HttpResponse, get_object_or_404, redirect

from demo.models import Employees, Student

from .forms import EmployeeForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    context = {
        'name': 'jayesh',
        'b_name': 'IT',
        'c_name': 'SVKM',
        'roll_no': 6,  # Use decimal format for clarity
        'sap_id': 14004210005
    }
    return render(request, 'aboutus.html', context)

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def Sum(request):
    if request.method == 'POST':
        try:
            am = int(request.POST['am'])
            ir = int(request.POST['ir'])
            ye = int(request.POST['ye'])
            result = (am * ir * ye) / 100
            return render(request, 'sum.html', {'result': result})
        except ValueError:
            return HttpResponse("Invalid input.")
    return HttpResponse("Method not allowed", status=405)

def sud(request):
    return render(request, 'student.html')

def msheet(request):
    if request.method == 'POST':
        try:
            s_name = request.POST['name']
            roll = int(request.POST['roll'])
            clg_name = request.POST['clg_name']
            clg_id = int(request.POST['clg_id'])
            phy = int(request.POST['phy'])
            chem = int(request.POST['chem'])
            math = int(request.POST['math'])
            eng = int(request.POST['eng'])
            mrt = int(request.POST['mrt'])
            total = phy + chem + math + eng + mrt
            per = (total / 500) * 100
            res = "pass" if all([phy >= 40, chem >= 40, math >= 40, eng >= 40, mrt >= 40]) else "fail"

            if per > 90 and res == "pass":
                grade = 'A+'
            elif per > 80 and res == "pass":
                grade = 'A'
            elif per > 60 and res == "pass":
                grade = 'B'
            elif per >= 40 and res == "pass":
                grade = 'C'
            else:
                grade = 'D'

            sheet = {
                "s_name": s_name,
                "roll": roll,
                "clg_name": clg_name,
                "clg_id": clg_id,
                "phy": phy,
                "chem": chem,
                "math": math,
                "eng": eng,
                "mrt": mrt,
                "total": total,
                "per": per,
                "res": res,
                "grade": grade
            }
            obj = Student(
                studentName=s_name, studentRollNo=roll, collegeId=clg_id, collegeName=clg_name,
                subject1Marks=phy, subject2Marks=chem, subject3Marks=math, subject4Marks=eng, subject5Marks=mrt,
                totalMarks=total, persentage=per, grade=grade
            )
            obj.save()
            msg = "Data is Saved Successfully"
            return render(request, 'result.html', {'sheet': sheet, 'msg': msg})
        except ValueError:
            return HttpResponse("Invalid input.")
    return HttpResponse("Method not allowed", status=405)

def employeePage(request):
    employees_list = Employees.objects.all()
    return render(request, 'employee.html', {'msg': employees_list})

def employeeDataSave(request):
    if request.method == 'POST':
        try:
            eName = request.POST['emp_Name']
            sal = int(request.POST['sal'])
            design = request.POST['designation']

            obj = Employees(empName=eName, salary=sal, designation=design)
            obj.save()
            return redirect('employee_page')  # Adjust to your actual URL pattern
        except ValueError:
            return HttpResponse("Invalid input.")
    return HttpResponse("Method not allowed", status=405)

def editEmployeeData(request, id):
    employee = get_object_or_404(Employees, id=id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee')  # Redirect to a list or detail view after saving
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'edit_emp.html', {'form': form, 'employee': employee})