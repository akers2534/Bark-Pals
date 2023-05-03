import React, { useState } from "react";

function SignUp() {
  const [selectedOption, setSelectedOption] = useState("");

  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };

  return (
    <div>
      <label>
        Select your sign up option:
        <select value={selectedOption} onChange={handleOptionChange}>
          <option value="">--Please choose an option--</option>
          <option value="sign-in">Sign In</option>
          <option value="join-the-community">Join The Community</option>
        </select>
      </label>
    </div>
  );
}

export default SignUp;
