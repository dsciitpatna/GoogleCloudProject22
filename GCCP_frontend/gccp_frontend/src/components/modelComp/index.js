import React from 'react'

const ModelComp = () => {
    return (
        <div className="modal-dialog modal-lg">
            <div className="modal-content my_modal_content">
                <div className="modal-header pull-right">
                    <button type="button" className="btn "><i className="fa fa-pencil" />    </button>
                    <button type="button" className="btn "><i className="fa fa-trash" /> </button>
                    <button type="button" className="btn " data-dismiss="modal" aria-label="Close">
                        <i className="fa fa-times" /> </button>
                    {/* <h4 class="modal-title">Add Checklist</h4> */}
                </div>
                <div style={{ clear: 'both' }} />
                <div className="modal-body">
                    <div className="row mb-10">
                        <div className="col-md-8">
                            <div className="event_dtl">
                                <div className="event_top">
                                    <div>
                                        <img src="dist/img/date.png" style={{ width: 126 }} />
                                    </div>
                                    <div className>
                                        <h2>Event Name</h2>
                                        <h4><i className="fa fa-clock-o" /> 4:00 PM-5:00PM</h4>
                                        <h4><i className="fa fa-map-marker" /> Tutorial Block-9, IIT Patna</h4>
                                        <h4><i className="fa fa-calendar" /> Calendar Name</h4>
                                    </div>
                                </div>
                                <p>LoremLorem ipsum dolor sit amet consectetur adipisicing elit. A repudiandae ullam sunt, nobis officia quod in placeat repellat? Magnam pariatur magni reiciendis in autem, sed laborum quidem rerum harum voluptatem error. Necessitatibus ad dignissimos enim sequi, quis laboriosam nostrum.</p>
                            </div>
                        </div>
                        <div className="col-md-4">
                            <div className="event_logo">
                                <img src="dist/img/event_logo.png" />
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    )
}

export default ModelComp