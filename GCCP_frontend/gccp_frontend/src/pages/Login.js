import React, { useEffect, useState } from "react";
import "../css/loginform.css";

const LoginForm = () => {
  const [popupStyle, showPopup] = useState("hide");

  const popup = () => {
    showPopup("login-popup");
    setTimeout(() => showPopup("hide"), 3000);
  };

  const onSuccess = (googleData) => {
    alert("User signed in");
    console.log(googleData);
  };

  const onFailure = (result) => {
    alert("User sign in Failed");
  };

  return (
    <div className="screen">
      <div className="cover1">
        <div className="picture"></div>
        <div className="txt2">
            <p>Schedule your meetings and priortise your tasks!</p>
            <p>Remain updated!</p>
        </div>
      </div>

      <div className="cover2">
        <div className="logo"></div>

        <div className="logintext">Login</div>
        <input type="text" placeholder="email" />
        <input type="password" placeholder="password" />

        <div className="login-btn" onClick={popup}>
          Login
        </div>
        <div className="forgot"><a href="">Forgot Password?</a></div>
        <p className="txt1">--------- Or login using ---------</p>

        <div className="alt-login">
          <div className="github"></div>
          <div className="google">
          </div>
        </div>

        <div className={popupStyle}>
          <h3>Login Failed</h3>
          <p>Username or password incorrect</p>
        </div>

        <div className="signup-container">
          <div className="signup-child txt">Don't have account?</div>
          <div className="signup-child btn">
            Signup
            </div>
        </div>
      </div>
    </div>
  );
};

export default LoginForm;
