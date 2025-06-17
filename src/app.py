"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
# Add more activities: 2 sports, 2 artistic, 2 intellectual
activities = {
    "Soccer Team": {
        "description": "Join the school soccer team for training and matches",
        "schedule": "Wednesdays and Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": []
    },
    "Basketball Club": {
        "description": "Practice basketball skills and compete in games",
        "schedule": "Tuesdays, 5:00 PM - 6:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "Art Club": {
        "description": "Explore painting, drawing, and other visual arts",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": []
    },
    "Drama Society": {
        "description": "Participate in acting, stage production, and school plays",
        "schedule": "Mondays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": []
    },
    "Math Olympiad": {
        "description": "Prepare for math competitions and solve challenging problems",
        "schedule": "Fridays, 2:00 PM - 3:30 PM",
        "max_participants": 25,
        "participants": []
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific topics",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Debate Team": {
        "description": "Engage in debates and improve public speaking skills",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "Robotics Club": {
        "description": "Build and program robots for competitions",
        "schedule": "Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 10,
        "participants": []
    },
    "Photography Club": {
        "description": "Learn photography techniques and participate in photo contests",
        "schedule": "Saturdays, 10:00 AM - 12:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Book Club": {
        "description": "Read and discuss various books and genres",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Cooking Class": {
        "description": "Learn cooking skills and explore different cuisines",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": []
    },
    "Music Band": {
        "description": "Practice and perform music in a band setting",
        "schedule": "Thursdays, 5:00 PM - 7:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Dance Troupe": {
        "description": "Learn various dance styles and perform at events",
        "schedule": "Wednesdays, 5:00 PM - 6:30 PM",
        "max_participants": 12,
        "participants": []
    },
    "Environmental Club": {
        "description": "Promote environmental awareness and sustainability",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Coding Bootcamp": {
        "description": "Intensive coding sessions to learn web development",
        "schedule": "Saturdays, 1:00 PM - 4:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Yoga Class": {
        "description": "Relax and improve flexibility through yoga",
        "schedule": "Mondays, 5:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Photography Workshop": {
        "description": "Hands-on photography skills and techniques",
        "schedule": "Sundays, 2:00 PM - 4:00 PM",
        "max_participants": 10,
        "participants": []
    },
    "Creative Writing": {
        "description": "Enhance writing skills through creative exercises",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    #Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up")
    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
