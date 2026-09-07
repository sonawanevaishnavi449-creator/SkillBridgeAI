import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SkillBridge AI",
    page_icon="🎓",
    layout="wide"
)

# ---------------- SAMPLE DATA ----------------
internships = [
    {
        "title": "Python Developer Intern",
        "company": "TechNova",
        "skills": ["Python", "SQL", "Git"],
        "location": "Remote"
    },
    {
        "title": "Data Science Intern",
        "company": "DataWorks",
        "skills": ["Python", "Pandas", "Machine Learning"],
        "location": "Pune"
    },
    {
        "title": "AI/ML Intern",
        "company": "InnovateAI",
        "skills": ["Python", "Machine Learning", "NumPy"],
        "location": "Mumbai"
    },
    {
        "title": "Web Development Intern",
        "company": "WebCraft",
        "skills": ["HTML", "CSS", "JavaScript"],
        "location": "Remote"
    }
]

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎓 SkillBridge AI")
st.sidebar.caption("From Classroom Skills to Industry Careers")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "👨‍🎓 Student Profile",
        "📝 Skill Assessment",
        "📊 Skill Gap Analysis",
        "💼 Internship Matching"
    ]
)

# ---------------- SESSION STATE ----------------
if "profile" not in st.session_state:
    st.session_state.profile = {}

if "scores" not in st.session_state:
    st.session_state.scores = {}

# ==================================================
# HOME
# ==================================================

if page == "🏠 Home":

    st.title("🎓 SkillBridge AI")
    st.subheader("From Classroom Skills to Industry Careers")

    st.write(
        "An AI-powered Academia–Industry collaboration platform "
        "that connects student skills with industry requirements."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Students", "1,250+")

    with col2:
        st.metric("Industry Opportunities", "150+")

    with col3:
        st.metric("Skills Tracked", "80+")

    st.divider()

    st.markdown("### 🔄 How SkillBridge AI Works")

    st.info(
        "ASSESS → BUILD SKILL PROFILE → FIND SKILL GAPS → "
        "RECOMMEND LEARNING → MATCH WITH INTERNSHIPS"
    )

    st.markdown("### 🎯 Problem We Solve")

    st.write(
        "Students often know theoretical concepts but do not know "
        "which skills industry expects. Companies also struggle to "
        "find candidates with the right skill combination."
    )

    st.success(
        "SkillBridge AI creates a continuous loop: "
        "Industry Demand → Student Skills → Skill Gap → Learning → Opportunity → Feedback"
    )


# ==================================================
# STUDENT PROFILE
# ==================================================

elif page == "👨‍🎓 Student Profile":

    st.title("👨‍🎓 Student Profile")

    name = st.text_input(
        "Full Name",
        value=st.session_state.profile.get("name", "")
    )

    branch = st.selectbox(
        "Branch",
        ["AI & Data Science", "Computer Engineering", "IT", "Electronics"]
    )

    year = st.selectbox(
        "Year",
        ["1st Year", "2nd Year", "3rd Year", "4th Year"]
    )

    skills = st.multiselect(
        "Your Skills",
        [
            "Python",
            "SQL",
            "Pandas",
            "NumPy",
            "Machine Learning",
            "HTML",
            "CSS",
            "JavaScript",
            "Git"
        ]
    )

    interest = st.selectbox(
        "Career Interest",
        [
            "Data Science",
            "AI / Machine Learning",
            "Software Development",
            "Web Development"
        ]
    )

    if st.button("💾 Save Profile", type="primary"):

        st.session_state.profile = {
            "name": name,
            "branch": branch,
            "year": year,
            "skills": skills,
            "interest": interest
        }

        st.success("✅ Profile saved successfully!")

    if st.session_state.profile:

        st.divider()
        st.subheader("Your Profile")

        p = st.session_state.profile

        st.write("**Name:**", p["name"])
        st.write("**Branch:**", p["branch"])
        st.write("**Year:**", p["year"])
        st.write("**Career Interest:**", p["interest"])
        st.write("**Skills:**", ", ".join(p["skills"]))


# ==================================================
# SKILL ASSESSMENT
# ==================================================

elif page == "📝 Skill Assessment":

    st.title("📝 Skill Assessment")

    st.write(
        "Answer these questions to estimate your current technical skill level."
    )

    st.divider()

    python_score = st.radio(
        "1. How comfortable are you with Python?",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    sql_score = st.radio(
        "2. How comfortable are you with SQL?",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    ml_score = st.radio(
        "3. How comfortable are you with Machine Learning?",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    pandas_score = st.radio(
        "4. How comfortable are you with Pandas?",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    if st.button("📊 Calculate Skill Score", type="primary"):

        level_value = {
            "Beginner": 40,
            "Intermediate": 70,
            "Advanced": 100
        }

        st.session_state.scores = {
            "Python": level_value[python_score],
            "SQL": level_value[sql_score],
            "Machine Learning": level_value[ml_score],
            "Pandas": level_value[pandas_score]
        }

        st.success("Assessment completed!")

        average = sum(st.session_state.scores.values()) / 4

        st.metric(
            "Overall Skill Score",
            f"{average:.0f}%"
        )

        st.progress(int(average))


# ==================================================
# SKILL GAP ANALYSIS
# ==================================================

elif page == "📊 Skill Gap Analysis":

    st.title("📊 Skill Gap Analysis")

    if not st.session_state.scores:

        st.warning(
            "⚠️ Please complete the Skill Assessment first."
        )

    else:

        st.write(
            "Based on your assessment, SkillBridge AI identifies "
            "skills that need improvement."
        )

        for skill, score in st.session_state.scores.items():

            st.write(f"### {skill}")

            st.progress(score)

            if score < 50:
                st.error("🔴 High Skill Gap")

            elif score < 80:
                st.warning("🟡 Moderate Skill Gap")

            else:
                st.success("🟢 Industry Ready")

        st.divider()

        st.subheader("💡 Recommended Learning")

        weak_skills = [
            skill
            for skill, score in st.session_state.scores.items()
            if score < 80
        ]

        if weak_skills:

            for skill in weak_skills:
                st.info(
                    f"📚 Improve **{skill}** through projects, "
                    f"practice and industry-oriented courses."
                )

        else:

            st.success(
                "🎉 Your current skill profile is strong!"
            )


# ==================================================
# INTERNSHIP MATCHING
# ==================================================

elif page == "💼 Internship Matching":

    st.title("💼 AI Internship Matching")

    if not st.session_state.profile:

        st.warning(
            "⚠️ Please create your Student Profile first."
        )

    else:

        student_skills = set(
            st.session_state.profile["skills"]
        )

        st.write(
            f"Matching opportunities for **{st.session_state.profile['name']}**"
        )

        st.divider()

        results = []

        for internship in internships:

            required = set(internship["skills"])

            matched = student_skills.intersection(required)

            score = (len(matched) / len(required)) * 100

            results.append(
                (
                    internship,
                    score,
                    matched,
                    required - student_skills
                )
            )

        results.sort(
            key=lambda x: x[1],
            reverse=True
        )

        for internship, score, matched, missing in results:

            st.subheader(
                f"💼 {internship['title']}"
            )

            st.write(
                f"**Company:** {internship['company']}"
            )

            st.write(
                f"**Location:** {internship['location']}"
            )

            st.metric(
                "Match Score",
                f"{score:.0f}%"
            )

            st.write(
                "**Matched Skills:**",
                ", ".join(matched) if matched else "None"
            )

            if missing:

                st.write(
                    "**Skill Gaps:**",
                    ", ".join(missing)
                )

            else:

                st.success(
                    "🎯 You have all required skills!"
                )

            st.divider()