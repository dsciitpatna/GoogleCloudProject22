import React from "react";
import { useUser } from "../Contexts/UserContext";
import { Navigate, Outlet } from "react-router-dom";
import Loading from "../components/Loading";

const PublicRoute = () => {
    const { loggedIn, loading } = useUser();
    return loading ? (
        <Loading />
    ) : loggedIn ? (
        <Navigate to="/calendar" replace />
    ) : (
        <Outlet />
    );
};

export default PublicRoute;
