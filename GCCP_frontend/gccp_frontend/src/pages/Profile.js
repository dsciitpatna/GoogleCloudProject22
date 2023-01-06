import "../css/addmember.css";
import * as React from "react";
import Sidebar from "../components/sidebar/index";
import Header from "../components/header/index";
import { ROLE } from "../components/util";
import { TextField } from "@mui/material";
import "../css/profile.css";
import { useState, useEffect } from "react";
import axios from "axios";

function Profile() {
    const [name, setName] = useState(""); // Name of the member
    const [email, setEmail] = useState(""); // Email of the member
    const [mobile, setMobile] = useState(""); // Mobile of the member
    const [position, setPosition] = useState(""); // Position of the member
    useEffect(() => {
        const fetchData = async () => {
            console.log("Hello World");
            const response = await axios.get(
                "http://127.0.0.1:8000/user/profile",
                {
                    withCredentials: true,
                }
            );

            const data = response.data;

            console.log(data);
            setName(data.name);
            setEmail(data.email);
            setMobile(data.ph_num);
            setPosition(ROLE[parseInt(data.role)]);
        };

        fetchData();
    }, []);

    return (
        <div className="sidebar-mini skin-black-light">
            <Header />
            <Sidebar />
            <div className="content-wrapper">
                <div class="content">
                    <link
                        href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css"
                        rel="stylesheet"
                    />
                    <div class="container profile-page">
                        <div class="row">
                            <div class="col-xl-6 col-lg-7 col-md-12">
                                <div class="card profile-header">
                                    <div class="body">
                                        <div class="row">
                                            <div class="col-lg-4 col-md-4 col-12">
                                                <div class="profile-image float-md-right">
                                                    {" "}
                                                    <img
                                                        src="https://bootdey.com/img/Content/avatar/avatar7.png"
                                                        alt=""
                                                    />{" "}
                                                </div>
                                            </div>
                                            <div class="col-lg-8 col-md-8 col-12">
                                                <TextField
                                                    id="name-of-member"
                                                    defaultValue="Name Surname"
                                                    label="Name"
                                                    InputProps={{
                                                        readOnly: true,
                                                        style: { fontSize: 15 },
                                                    }}
                                                    value={name}
                                                    sx={{
                                                        width: "100%",
                                                        mt: 3,
                                                    }}
                                                    InputLabelProps={{
                                                        style: { fontSize: 12 },
                                                    }}
                                                />

                                                <TextField
                                                    id="email-of-member"
                                                    defaultValue="Email@email.com"
                                                    label="Email"
                                                    InputProps={{
                                                        readOnly: true,
                                                        style: { fontSize: 15 },
                                                    }}
                                                    value={email}
                                                    sx={{
                                                        width: "100%",
                                                        mt: 3,
                                                    }}
                                                    InputLabelProps={{
                                                        style: { fontSize: 12 },
                                                    }}
                                                />

                                                <TextField
                                                    id="Mobile-of-member"
                                                    defaultValue="1234567890"
                                                    label="Mobile No."
                                                    InputProps={{
                                                        readOnly: true,
                                                        style: { fontSize: 15 },
                                                    }}
                                                    value={mobile}
                                                    sx={{
                                                        width: "100%",
                                                        mt: 3,
                                                    }}
                                                    InputLabelProps={{
                                                        style: { fontSize: 12 },
                                                    }}
                                                />

                                                <TextField
                                                    id="position-of-member"
                                                    defaultValue="Club Coordinator"
                                                    label="Position"
                                                    InputProps={{
                                                        readOnly: true,
                                                        style: { fontSize: 15 },
                                                    }}
                                                    value={position}
                                                    sx={{
                                                        width: "100%",
                                                        mt: 3,
                                                    }}
                                                    InputLabelProps={{
                                                        style: { fontSize: 12 },
                                                    }}
                                                />
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Profile;
