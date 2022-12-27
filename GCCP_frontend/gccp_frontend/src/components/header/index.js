import React from 'react'

const Header = () => {
    return (
        <header className="main-header">
            {/* Logo */}
            <a href="#" className="logo">
                {/* mini logo for sidebar mini 50x50 pixels */}
                <span className="logo-mini"><b>Logo</b> </span>
                {/* logo for regular state and mobile devices */}
                <span className="logo-lg"><b>Logo</b> </span>
            </a>
            {/* Header Navbar: style can be found in header.less */}
            <nav className="navbar navbar-static-top">
                {/* Sidebar toggle button*/}
                <a href="#" className="sidebar-toggle" data-toggle="push-menu" role="button">
                    <span className="sr-only">Toggle navigation</span>
                </a>
                <a href="#" className="int_people">
                    <i className="fa fa-user-plus" />
                    Invite people
                </a>
                <div className="navbar-custom-menu">
                    <ul className="nav navbar-nav">
                        <li className="dropdown messages-menu">
                        </li>
                        <li className="dropdown user user-menu">
                            <a href="#" className="dropdown-toggle" data-toggle="dropdown">
                                <img src="dist/img/user-img.png" className="user-image" alt="User Image" />
                            </a>
                        </li>
                    </ul>
                </div>
            </nav>

        </header>
    )
}

export default Header