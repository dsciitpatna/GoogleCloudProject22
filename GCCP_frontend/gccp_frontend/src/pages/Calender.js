import React from "react";
import { Calendar, momentLocalizer } from "react-big-calendar";
import moment from "moment";
import "react-big-calendar/lib/css/react-big-calendar.css";

import events from '../config/events'
import Sidebar from '../components/sidebar/index'
import Header from '../components/header/index'
// Setup the localizer by providing the moment (or globalize, or Luxon) Object
// to the correct localizer.
const localizer = momentLocalizer(moment);

// const events = [
//   {
//     start: moment().toDate(),
//     end: moment().toDate(),
//     title: "Event 1",
//   },
// ];

const Calender = () => {
  return (
    <div className="sidebar-mini skin-black-light">
      <Header />
      <Sidebar/>
      <div className="content-wrapper">
        
      <div class="content">
      <Calendar
        localizer={localizer}
        defaultDate={new Date()}
        defaultView="month"
        events={events}
        style={{ height: "100vh" }}
      />
    </div>
    </div>
    </div>
  );
};

export default Calender;
