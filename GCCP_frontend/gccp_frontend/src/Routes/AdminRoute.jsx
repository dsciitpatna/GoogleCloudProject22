import React, { useEffect } from "react";
import { useUser } from "../Contexts/UserContext";
import { Navigate, Outlet } from "react-router-dom";
import Loading from "../components/Loading";

const AdminRoute = () => {
    const { loggedIn, loading, user } = useUser();

    useEffect(() => {
        console.log(`LOADING: ${loading}; LOGGED_IN: ${loggedIn}`);
    }, [loading, loggedIn]);

    return loading ? (
        <Loading />
    ) : (!loggedIn || user.role !== '0') ? (
        <Navigate to="/login" replace />
    ) : (
        <Outlet />
    );
};

export default AdminRoute;

