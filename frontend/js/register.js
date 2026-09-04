// ==========================================
// REGISTER PAGE
// ==========================================

const form = document.getElementById("registerForm");


// ==========================================
// REGISTER FORM SUBMIT
// ==========================================

form.addEventListener("submit", async (e) => {

    e.preventDefault();


    // Get form values

    const username =
        document.getElementById("username").value.trim();

    const email =
        document.getElementById("email").value.trim();

    const password =
        document.getElementById("password").value;

    const confirmPassword =
        document.getElementById("confirmPassword").value;


    // ==========================================
    // BASIC VALIDATION
    // ==========================================

    if (!username || !email || !password || !confirmPassword) {

        alert("Please fill all fields.");

        return;
    }


    if (password !== confirmPassword) {

        alert("Passwords do not match!");

        return;
    }


    if (password.length < 6) {

        alert("Password must contain at least 6 characters.");

        return;
    }


    // ==========================================
    // SEND DATA TO BACKEND
    // ==========================================

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/users/register",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    username: username,
                    email: email,
                    password: password
                })
            }
        );


        const data = await response.json();


        console.log(
            "Registration Status:",
            response.status
        );

        console.log(
            "Registration Response:",
            data
        );


        // ==========================================
        // SUCCESS
        // ==========================================

        if (response.ok) {

            alert(
                data.message ||
                "Registration Successful!"
            );


            // Go to Login page

            window.location.href = "login.html";

        }


        // ==========================================
        // BACKEND ERROR
        // ==========================================

        else {

            alert(
                data.detail ||
                data.message ||
                "Registration Failed!"
            );
        }


    } catch (error) {

        console.error(
            "Registration Error:",
            error
        );

        alert(
            "Unable to connect to the backend."
        );
    }

});