import React, { useEffect } from "react";
import { useUser } from "../Contexts/UserContext";
import { Navigate, Outlet } from "react-router-dom";
import Loading from "../components/Loading";

const ClubAdminRoute = () => {
    const { loggedIn, loading, user } = useUser();

    useEffect(() => {
        console.log(`LOADING: ${loading}; LOGGED_IN: ${loggedIn}`);
    }, [loading, loggedIn]);

    return loading ? (
        <Loading />
    ) : (!loggedIn || user.role !== '1') ? (
        <Navigate to="/login" replace />
    ) : (
        <Outlet />
    );
};

export default ClubAdminRoute;


