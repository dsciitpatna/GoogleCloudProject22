import React from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { useUser } from "../../Contexts/UserContext";

const SideBar = () => {
    const navigate = useNavigate();
    const { setLoggedIn } = useUser();
    const handleLogOut = async (e) => {
        e.preventDefault();
        const url = `${process.env.REACT_APP_HOST}/user/logout`;
        try {
            await axios.delete(url, { withCredentials: true });
            setLoggedIn(false);
            navigate("/");
        } catch (e) {
            console.error(e);
        }
    };
    return (
        <aside className="main-sidebar">
            {/* sidebar: style can be found in sidebar.less */}
            <section className="sidebar">
                {/* /.search form */}
                {/* sidebar menu: : style can be found in sidebar.less */}
                <ul className="sidebar-menu" data-widget="tree">
                    <li>
                        <Link to="/">
                            <i className="fa fa-home" />
                            <span>Home</span>
                        </Link>
                    </li>
                    <li>
                        <Link to="/">
                            <i className="fa fa-calendar" />
                            <span>My Task</span>
                        </Link>
                    </li>
                    <li className>
                        <Link to="/profile">
                            <i className="fa fa-bell" />
                            <span>Profile</span>
                        </Link>
                    </li>
                    <li className="header">Favourites</li>
                    <li>
                        <a href="#">
                            <i className="fa fa-circle text-red" />{" "}
                            <span>Quizzes</span>
                        </a>
                    </li>
                    <li>
                        <Link to="/technical">
                            <i className="fa fa-circle text-yellow" />{" "}
                            <span>Technical </span>
                        </Link>
                    </li>
                    <li>
                        <a href="#">
                            <i className="fa fa-circle text-aqua" />{" "}
                            <span>Cultural</span>
                        </a>
                    </li>
                    <li>
                        <a href="#">
                            <i className="fa fa-circle text-green" />{" "}
                            <span>Sports</span>
                        </a>
                    </li>
                    <li>
                        <a href="#">
                            <i className="fa fa-circle text-blue" />{" "}
                            <span>General </span>
                        </a>
                    </li>
                    <li className>
                        <a href="#" style={{ color: "black", fontSize: 16 }}>
                            <i className="fa fa-plus" />
                            <span>Add Item</span>
                        </a>
                    </li>
                    <li className>
                        <a href="#" style={{ color: "black", fontSize: 20 }}>
                            <i className="fa fa-user-plus" />
                            <span> Invite people</span>
                        </a>
                    </li>
                    <li>
                        <a
                            href="#"
                            style={{ color: "black", fontSize: 16 }}
                            onClick={handleLogOut}
                        >
                            <i className="fa fa-sign-out" />{" "}
                            <span> Logout</span>
                        </a>
                    </li>
                </ul>
            </section>
            {/* /.sidebar */}
        </aside>
    );
};

export default SideBar;
