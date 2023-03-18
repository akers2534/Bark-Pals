import React, { useState } from "react";

const Login = () => {
  const [username, setusername] = useState("");
  const [password, setpassword] = useState("");
  function handel_submit(e) {
    e.preventDefault();
  }
  return <form onSubmit={handel_submit}>Login</form>;
};

export default Login;
