import { useState } from "react";
import axios from "axios";

function Signup() {
    const [formData, setFormData] = useState({ username: "", email: "", password: "" });

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post("http://localhost:8000/auth/signup", formData);
            alert("Signup Successful!");
        } catch (error) {
            alert(error.response.data.detail);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="Username" onChange={(e) => setFormData({ ...formData, username: e.target.value })} />
            <input type="email" placeholder="Email" onChange={(e) => setFormData({ ...formData, email: e.target.value })} />
            <input type="password" placeholder="Password" onChange={(e) => setFormData({ ...formData, password: e.target.value })} />
            <button type="submit">Signup</button>
        </form>
    );
}

export default Signup;
