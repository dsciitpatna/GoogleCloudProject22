import axios from "axios";
import React, { useContext, createContext, useState, useEffect } from "react";

const UserContext = createContext();

const useUser = () => {
    const context = useContext(UserContext);
    if (context === undefined) {
        throw new Error("useUser must be used within a UserProvider");
    }
    return context;
};

export const UserProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loggedIn, setLoggedIn] = useState(false);
    const [loading, setLoading] = useState(true);
    const value = { user, setUser, loggedIn, setLoggedIn, setLoading, loading };

    useEffect(() => {
        const getUser = async () => {
            setLoading(true);
            try {
                const { data } = await axios.get(
                    `${process.env.REACT_APP_HOST}/user/get-user`,
                    { withCredentials: true }
                );
                if (data.message) {
                    setUser(null);
                    setLoggedIn(false);
                } else {
                    setUser(data);
                    setLoggedIn(true);
                }
            } catch (e) {
                console.error(e);
                setUser(null);
                setLoggedIn(false);
            } finally {
                setLoading(false);
            }
        };

        getUser();
    }, []);

    return (
        <UserContext.Provider value={value}>{children}</UserContext.Provider>
    );
};

export { useUser };
