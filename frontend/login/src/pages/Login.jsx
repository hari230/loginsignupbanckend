import { useState } from "react";
import axios from "axios";

function Login() {
    const [formData, setFormData] = useState({ email: "", password: "" });

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://localhost:8000/auth/login", formData);
            alert("Login Successful! Token: " + response.data.access_token);
        } catch (error) {
            alert(error.response.data.detail);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="email" placeholder="Email" onChange={(e) => setFormData({ ...formData, email: e.target.value })} />
            <input type="password" placeholder="Password" onChange={(e) => setFormData({ ...formData, password: e.target.value })} />
            <button type="submit">Login</button>
        </form>
    );
}

export default Login;
