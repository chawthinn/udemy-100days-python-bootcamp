# footer_utils.py

def load_footer(day_number):
    """
    Load the footer HTML content and dynamically insert the day number.
    Adds a horizontal divider (<hr>) before the footer content.
    """
    # HTML Content with Dynamic Day Number and Footer Styles
    footer_content = f"""
    <div class="footer">
        <p>💻 This is the Day {day_number} Project from the <a href="https://www.udemy.com/course/100-days-of-code/" target="_blank">100 Days of Code</a> course by Dr. Angela.</p><br>
        <p>👋 <b>About Me:</b><br>
            Hi there! I’m Chaw, a Product Manager with 5 years of experience.<br>
            I’m now studying Big Data Analytics in Lambton College, aspiring to become a Data Scientist.
            <br>I've started sharing TL;DR versions of my projects and tutorials.
            <br>Let's connect over a coffee chat! ☕</p><br>
        <p>🔗 <b>My Socials:</b><br>
            <a href="https://linkedin.com/in/chawthinn" target="_blank">🌐 LinkedIn</a> | 
            <a href="https://github.com/chawthinn" target="_blank">🐙 GitHub</a> | 
            <a href="https://medium.com/@chawthinn" target="_blank">✍️ Medium</a> | 
            <a href="https://share.streamlit.io/user/chawthinn" target="_blank">🚀 Streamlit Apps</a>
        </p><br>
        <p>🛠 Tech Stack:<br>
            - Built with Python 3.12.7<br>
            - Powered by Streamlit 1.39.0<br>
        </p>
        <p>📝 Open-sourced under the MIT License<br>
        Copyright (c) 2024 Chaw Thinn</p>
    </div>
    """

    footer_css = """
    <style>
    .footer {
        position: relative;
        bottom: 0;
        width: 100%;
        text-align: center;
        font-size: 14px;
        padding: 20px 10px;
        background-color: #0e1117;
        color: #d1d1d1;
        border-top: 1px solid #3b4049;
    }

    .footer h4 {
        color: #ffffff;
        margin-bottom: 10px;
        font-size: 16px;
        font-weight: bold;
    }

    .footer a {
        color: #4F8BF9;
        text-decoration: none;
        font-weight: bold;
    }

    .footer a:hover {
        text-decoration: underline;
    }

    .footer p {
        margin: 5px 0;
    }

    .footer .license {
        font-size: 12px;
        margin-top: 15px;
    }
    </style>
    """

    # Combine HTML and CSS
    full_footer = footer_css + footer_content
    return full_footer
