import React, { useEffect, useState } from "react";
import "../css/signupform.css";

const SignupForm = () => {

  const [popupStyle, showPopup] = useState("hide");

  const popup = () => {
    showPopup("login-popup");
    setTimeout(() => showPopup("hide"), 3000);
  };

  const onSuccess = (e) => {
    alert("User signed in");
    console.log(e);
  };

  const onFailure = (e) => {
    alert("User sign in Failed");
    console.log(e);
  };


  return (
    <div className="screen">
      <div className="cover1">
        <div className="logo1"></div>
        <div className="txt1">
            <p>Create your account today!</p>
        </div>
        <div className="alternative">
           <div className="github">Sign up with GitHub</div>
           <div className="google">Sign up with Google
            {/* <GoogleLogin
              className="white"
              clientId="79474543031-tmjo35916ufn421ej3u1i2ljao2apr4s.apps.googleusercontent.com"
              buttonText=""
              onSuccess={onSuccess}
              onFailure={onFailure}
              cookiePolicy={"single_host_origin"}
              isSignedIn={false} // alternative is true, which keeps the user signed in
              icon={false} // alt is true, and this puts the google logo on your button, but I don't like it
              theme="dark" // alternative is light, which is white
            /> */}
          </div> 
        </div>
      </div>

      <div className="cover2">
        <div className="logo2"></div>

        <div className="signuptext">Sign up</div>
        <input type="text" placeholder="name" />
        <input type="text" placeholder="email" />
        <input type="password" placeholder="password" />

        <div className="signup-btn" onClick={popup}>
          Sign up
        </div>

        <div className="login-container">
          <div className="login-child txt">Already a member?</div>
          <div className="login-child btn">
            Login
            </div>
        </div>
      </div>
    </div>
  );
};

export default SignupForm;
