import React, { useEffect, useState } from 'react'
import Header from '../header'
import SideBar from '../sidebar'
import { membersData, adminsData } from "./data"
const Members = () => {
    const [activeTab, setActiveTab] = useState("member")
    const [listData, setListData] = useState([])
    const [tempSearch, setTempSearch] = useState("")
    // const [count, setCount] = useState(0)
    

    useEffect(() => {
        loadMembers()
    }, [])
    useEffect(() => {
        if (tempSearch) {
            const filterlist = listData.filter(item => item.name.toLowerCase().includes(tempSearch.toLowerCase()) || item.email.toLowerCase().includes(tempSearch.toLowerCase()))
            setListData(filterlist)
        } else {
            if (activeTab === "member")
                setListData(membersData)
            else
                setListData(adminsData)
        }
    }, [tempSearch])

    const loadAdmins = () => {
        setActiveTab("admin")
        setListData(membersData)
    }
    const loadMembers = () => {
        setActiveTab("member")
        setListData(adminsData)
    }
    return (
        <div className="sidebar-mini skin-black-light">
            <div className="wrapper">
                <Header />
                {/* Left side column. contains the logo and sidebar */}
                <SideBar />
                {/* Content Wrapper. Contains page content */}
                <div className="content-wrapper">

                    {/* Main content */}
                    <section className="content">
                        <div className="row">
                            {/* Left col */}
                            <div className="col-lg-12">
                                <div className="tab_bar">
                                    <div className="tab_bar_left">
                                        <a href="#" className={activeTab === "member" ? "active" : ""} onClick={() => loadMembers()} >Members</a>
                                        <a href="#" className={activeTab === "admin" ? "active" : ""} onClick={() => loadAdmins()}>Admins</a>
                                    </div>
                                    <div className="tab_bar_right">
                                        <i className="fa fa-search" />
                                        <input type="text" name="table_search" value={tempSearch} onChange={(e) => setTempSearch(e.target.value)} className="form-control " placeholder="Search by name" />
                                    </div>
                                </div>
                                <div className="page_tilte">
                                    <h3>Members  <a href="#">Add New</a></h3>
                                </div>
                                <div className="my_table" style={{ "overflow": "auto" }}>
                                    <table className="table table-responsive ">
                                        <tbody>
                                            <tr>
                                                <th>Photo</th>
                                                <th>Name</th>
                                                <th>Email</th>
                                                <th>Mobile </th>
                                                <th>Post</th>
                                            </tr>
                                            {listData.map((item, index) => (
                                                <>
                                                    <tr>
                                                        <td>
                                                            <div className="user-block"><img className="img-circle img-bordered-sm" src="dist/img/user1-128x128.jpg" alt="user image" /></div>
                                                        </td>
                                                        <td>{item.name}</td>
                                                        <td>{item.email}</td>
                                                        <td>{item.mobile} </td>
                                                        <td>{item.post} </td>
                                                    </tr>
                                                </>
                                            ))}


                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </section>
                    {/* /.content */}
                </div>
            </div>
        </div>
    )
}

export default Members