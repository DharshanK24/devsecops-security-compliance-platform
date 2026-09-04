const form = document.getElementById("loginForm");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/users/login",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },

                body: JSON.stringify({
                    email: email,
                    password: password
                })
            }
        );

        const data = await response.json();

        console.log("Login Status:", response.status);
        console.log("Login Response:", data);


        // ==========================================
        // LOGIN SUCCESS
        // ==========================================

        if (response.ok) {

            // Get JWT access token
            const token = data.access_token;

            console.log(
                "Access Token:",
                token ? "TOKEN RECEIVED" : "TOKEN NOT RECEIVED"
            );


            // ==========================================
            // CHECK TOKEN
            // ==========================================

            if (!token) {

                console.error(
                    "JWT token missing. Backend response:",
                    data
                );

                alert(
                    "Login successful, but JWT token was not received."
                );

                return;
            }


            // ==========================================
            // SAVE JWT TOKEN
            // ==========================================

            localStorage.setItem(
                "access_token",
                token
            );


            // Check saved token
            const savedToken =
                localStorage.getItem("access_token");

            console.log(
                "JWT saved:",
                savedToken ? "YES" : "NO"
            );


            // ==========================================
            // LOGIN SUCCESS
            // ==========================================

            alert("Login Successful!");


            // Go to Dashboard
            window.location.href = "dashboard.html";

        }


        // ==========================================
        // LOGIN FAILED
        // ==========================================

        else {

            alert(
                data.detail ||
                data.message ||
                "Login Failed!"
            );
        }


    } catch (error) {

        console.error(
            "Login Error:",
            error
        );

        alert(
            "Unable to connect to backend."
        );
    }
});