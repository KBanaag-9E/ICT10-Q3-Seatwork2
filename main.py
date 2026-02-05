from pyscript import display, document

def check_requirements(e):

    registration = document.querySelector("input[name='reg']:checked").value
    medical_clearance = document.querySelector("input[name='med']:checked").value
    grade_level = document.getElementById("grade-level").value
    section = document.getElementById("section").value

    document.getElementById("output").innerHTML = ' '
    document.getElementById("team_photo").innerHTML = ' '

    if (grade_level == "g7" or grade_level == "g8" or grade_level == "g9" or  grade_level == "g10") and section == "e" and registration == "yes" and medical_clearance == "yes":
        display(f"You are part of the", target='output')
        document.getElementById("team_photo").innerHTML = "<img src='green_hornets.jpeg' height='250px' width='100px'>"
    elif (grade_level == "g7" or grade_level == "g8" or grade_level == "g9" or  grade_level == "g10") and section == "r" and registration == "yes" and medical_clearance == "yes":
        display(f"You are part of the", target='output')
        document.getElementById("team_photo").innerHTML = "<img src='red_bulldogs.jpeg' height='250px' width='100px'>"
    elif (grade_level == "g7" or grade_level == "g8" or grade_level == "g9" or  grade_level == "g10") and section == "s" and registration == "yes" and medical_clearance == "yes":
        display(f"You are part of the", target='output')
        document.getElementById("team_photo").innerHTML = "<img src='blue_bears.jpeg' height='250px' width='100px'>"
    elif (grade_level == "g7" or grade_level == "g8" or grade_level == "g9" or  grade_level == "g10") and section == "t" and registration == "yes" and medical_clearance == "yes":
        display(f"You are part of the", target='output')
        document.getElementById("team_photo").innerHTML = "<img src='yellow_tigers.jpeg' height='250px' width='100px'>"
    else:
        document.getElementById("output").innerHTML = "You are not qualified to participate in the OBMC Intramurals."
