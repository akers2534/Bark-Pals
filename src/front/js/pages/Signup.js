import React, { useState } from "react";

export const Signup = () => {
  const [username, setusername] = useState("");
  const [password, setpassword] = useState("");
  function handel_submit(e) {
    e.preventDefault();
  }
  return (
    <div className="row">
      <form className="mx-auto col-6 pt-5">
        <div class="form-outline mb-4">
          <input type="email" id="form2Example1" class="form-control" />
          <label class="form-label" for="form2Example1">
            Email address
          </label>
        </div>

        <div class="form-outline mb-4">
          <input type="password" id="form2Example2" class="form-control" />
          <label class="form-label" for="form2Example2">
            Password
          </label>
        </div>

        <button type="button" class="btn btn-primary btn-block mb-4">
          Sign Up!
        </button>

        <div class="text-center">
          <button type="button" class="btn btn-link btn-floating mx-1">
            <i class="fab fa-facebook-f"></i>
          </button>

          <button type="button" class="btn btn-link btn-floating mx-1">
            <i class="fab fa-google"></i>
          </button>

          <button type="button" class="btn btn-link btn-floating mx-1">
            <i class="fab fa-twitter"></i>
          </button>

          <button type="button" class="btn btn-link btn-floating mx-1">
            <i class="fab fa-github"></i>
          </button>
        </div>
      </form>
    </div>
  );
};
