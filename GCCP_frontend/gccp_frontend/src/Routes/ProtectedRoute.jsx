import React, { useEffect } from "react";
import { useUser } from "../Contexts/UserContext";
import { Navigate, Outlet } from "react-router-dom";
import Loading from "../components/Loading";

const ProtectedRoute = () => {
    const { loggedIn, loading } = useUser();

    useEffect(() => {
        console.log(`LOADING: ${loading}; LOGGED_IN: ${loggedIn}`);
    }, [loading, loggedIn]);

    return loading ? (
        <Loading />
    ) : !loggedIn ? (
        <Navigate to="/login" replace />
    ) : (
        <Outlet />
    );
};

export default ProtectedRoute;
