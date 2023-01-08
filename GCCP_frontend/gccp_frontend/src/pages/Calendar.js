import React from "react";
import { formatDate } from "@fullcalendar/core";
import FullCalendar from "@fullcalendar/react";
import dayGridPlugin from "@fullcalendar/daygrid";
import timeGridPlugin from "@fullcalendar/timegrid";
import interactionPlugin from "@fullcalendar/interaction";
import { INITIAL_EVENTS, createEventId } from "../config/events";
import Sidebar from "../components/sidebar/index";
import Header from "../components/header/index";
import ModelComp from "../components/modelComp";

import "../css/calendar.css";

export default function DemoApp() {
    // state = {
    //   weekendsVisible: true,
    //   currentEvents: [],
    //   showModal: false,
    // };

    const [weekendsVisible, setWeekendsVisible] = React.useState(true);
    const [currentEvents, setCurrentEvents] = React.useState([]);
    const [showModal, setShowModal] = React.useState(false);

    const handleWeekendsToggle = () => {
        setWeekendsVisible(!weekendsVisible);
    };

    const handleDateSelect = (selectInfo) => {
        let title = prompt("Please enter a new title for your event");
        let calendarApi = selectInfo.view.calendar;

        calendarApi.unselect(); // clear date selection

        if (title) {
            calendarApi.addEvent({
                id: createEventId(),
                title,
                start: selectInfo.startStr,
                end: selectInfo.endStr,
                allDay: selectInfo.allDay,
            });
        }
    };

    const handleEventClick = (clickInfo) => {
        setShowModal(true);
    };

    const handleEvents = (events) => {
        setCurrentEvents(events);
    };

    return (
        <div className="demo-app sidebar-mini skin-black-light">
            <Header />
            <Sidebar />
            <div className="content-wrapper">
                {/* {renderSidebar()} */}
                <div className="demo-app-main content">
                    <FullCalendar
                        plugins={[
                            dayGridPlugin,
                            timeGridPlugin,
                            interactionPlugin,
                        ]}
                        headerToolbar={{
                            left: "prev,next today",
                            center: "title",
                            right: "dayGridMonth,timeGridWeek,timeGridDay",
                        }}
                        initialView="dayGridMonth"
                        editable={true}
                        selectable={true}
                        selectMirror={true}
                        dayMaxEvents={true}
                        weekends={weekendsVisible}
                        initialEvents={INITIAL_EVENTS} // alternatively, use the `events` setting to fetch from a feed
                        select={handleDateSelect}
                        eventContent={renderEventContent} // custom render function
                        eventClick={handleEventClick}
                        eventsSet={handleEvents} // called after events are initialized/added/changed/removed
                        /* you can update a remote database when these fire:
            eventAdd={function(){}}
            eventChange={function(){}}
            eventRemove={function(){}}
            */
                    />
                    {showModal ? (
                        <div
                            className="modal fade in"
                            style={{ display: "block" }}
                        >
                            <ModelComp closeHandler={setShowModal} />
                        </div>
                    ) : null}
                </div>
            </div>
        </div>
    );

    function renderSidebar() {
        return (
            <div className="demo-app-sidebar">
                <div className="demo-app-sidebar-section">
                    <h2>Instructions</h2>
                    <ul>
                        <li>
                            Select dates and you will be prompted to create a
                            new event
                        </li>
                        <li>Drag, drop, and resize events</li>
                        <li>Click an event to delete it</li>
                    </ul>
                </div>
                <div className="demo-app-sidebar-section">
                    <label>
                        <input
                            type="checkbox"
                            checked={weekendsVisible}
                            onChange={handleWeekendsToggle}
                        ></input>
                        toggle weekends
                    </label>
                </div>
                <div className="demo-app-sidebar-section">
                    <h2>All Events ({currentEvents.length})</h2>
                    <ul>{currentEvents.map(renderSidebarEvent)}</ul>
                </div>
            </div>
        );
    }
}

function renderEventContent(eventInfo) {
    return (
        <>
            <b>{eventInfo.timeText}</b>
            <i>{eventInfo.event.title}</i>
        </>
    );
}

function renderSidebarEvent(event) {
    return (
        <li key={event.id}>
            <b>
                {formatDate(event.start, {
                    year: "numeric",
                    month: "short",
                    day: "numeric",
                })}
            </b>
            <i>{event.title}</i>
        </li>
    );
}
