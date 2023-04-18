const url_beacon_data_collect = "http://localhost:8000/v1/beacon/"

let page_start_date = new Date();
let beacon = {
    page_location: window.location.href,
    page_start: page_start_date.toISOString(),
    page_end: null,
    events: [
        {
            event_name: 'page_view',
            timestamp: new Date().toISOString(),
        }
    ]
}


document.addEventListener('click', (el) => {
    el.preventDefault();
    if (el.target.id) {
        try {
            // the event data is pushed to the beacon.events list
            beacon.events.push({
                event_name: `${el.target.id}-clicked`,
                timestamp: new Date().toISOString(),
            });
            console.log(beacon);
        } catch (error) {
            console.log(error);
        }
    }

});

// at visibility change
// a) if the user left the page (visibility was changed to 'hidden')
// then append page_end and send data to server
// also empty the beacon data by setting it to {} to be safe (as the data has been already sent to server)

// b) if the user came back to the page (visibility was changed to 'visible')
// re-initialize the beacon data as this is a new user visit
document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') {
        try {
            beacon.page_end = new Date().toISOString()
            console.log("beacon sent", beacon)
            const data = new Blob([JSON.stringify(beacon)], {type: 'application/json'});
            navigator.sendBeacon(url_beacon_data_collect, data);
            beacon = {};
        } catch (error) {
            console.log("beacon failed", error);
        }
    }
    if (document.visibilityState === 'visible') {
        console.log("returned back to the same page")
        beacon = {
            page_location: window.location.href,
            page_start: new Date().toISOString(),
            page_end: null,
            events: [
                {
                    event_name: 'page_view',
                    timestamp: new Date().toISOString(),
                },
            ]
        };
    }
});
