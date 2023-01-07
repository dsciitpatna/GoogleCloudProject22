import "./App.css";
import Login from "./pages/Login";
import { UserProvider } from "./Contexts/UserContext";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import ProtectedRoute from "./Routes/ProtectedRoute";
import PublicRoute from "./Routes/PublicRoute";

import CreateEvent from "./pages/CreateEvent";
import Members from "./components/members";
import AddMember from "./pages/AddMember";
import Calendar from "./pages/Calendar";
import Technical from "./components/technical/index";
import SignupForm from "./pages/Signup";
import Profile from "./pages/Profile";

function App() {
    // <div className="App">
    //   <header className="App-header">
    //     <Login/>
    //   </header>
    // </div>
    return (
        <UserProvider>
            <BrowserRouter>
                <Routes>
                    <Route path="/login" element={<PublicRoute />}>
                        <Route path="/login" element={<Login />} />
                    </Route>
                    <Route path="/Signup" element={<SignupForm />} />
                    <Route path="/" element={<ProtectedRoute />}>
                        <Route
                            path=""
                            element={<Navigate to="/calendar" replace />}
                        />
                        <Route path="/calendar" element={<Calendar />} />
                        <Route path="/CreateEvent" element={<CreateEvent />} />
                        <Route path="/members" element={<Members />} />
                        <Route path="/AddMember" element={<AddMember />} />
                        <Route
                            exact
                            path="/technical"
                            element={<Technical />}
                        />
                        <Route path="/Profile" element={<Profile />} />
                    </Route>
                    <Route
                        path="*"
                        element={<Navigate to="/calendar" replace />}
                    />
                </Routes>
            </BrowserRouter>
        </UserProvider>
    );
}

export default App;
