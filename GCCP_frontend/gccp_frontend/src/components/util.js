const HOST = process.env.REACT_APP_HOST;

const ROLE = ["Admin", "Club Admin", "Student"];
const handleGOauth = (event) => {
    // bind a link for google oauth
    event.preventDefault();
    const location = `${HOST}/accounts/google/login/`;
    window.location = location;
  }
export {ROLE, handleGOauth};
