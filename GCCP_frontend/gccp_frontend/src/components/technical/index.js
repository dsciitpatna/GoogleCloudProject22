import React from 'react'
import Header from '../header'
import ModelComp from '../modelComp'
import SideBar from '../sidebar'

const Technical = () => {
    return (
        <div className='sidebar-mini skin-black-light'>

            <div className="wrapper">
                <Header />
                {/* Left side column. contains the logo and sidebar */}
                <SideBar />
                {/* Content Wrapper. Contains page content */}
                <div className="content-wrapper">
                    {/* Content Header (Page header) */}
                    <section className="content-header inline-block">
                        <h1 className>Technical <small /></h1>
                    </section>
                    {/* Main content */}
                    <section className="content">
                        <div className="row">
                            {/* Left col */}
                            <div className="col-lg-12">
                                <div className="nav-tabs-custom">
                                    <ul className="nav nav-tabs">
                                        <li><a href="#" data-toggle="tab">Overview</a></li>
                                        <li><a href="#" data-toggle="tab">List</a></li>
                                        <li><a href="#" data-toggle="tab">Status</a></li>
                                        <li className="active"><a href="#" data-toggle="tab">Timeline</a></li>
                                        <li><a href="#" data-toggle="tab">Calender</a></li>
                                        <li><a href="#" data-toggle="tab">More</a></li>
                                        <li className="pull-right myBtn">
                                            <button className="btn btn-primary" data-toggle="modal" data-target="#AddProject"><i className="fa fa-plus" /> Add section</button>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        {/* Add New Checklist */}
                        <div className="modal fade" id="AddProject">
                        <ModelComp/>
                        </div>
                    </section>
                    {/* /.content */}
                </div>

            </div>

        </div>
    )
}

export default Technical