import Navbar from '../components/Navbar'
import '../css/viewmembers.css'
import * as React from 'react';
import ViewMembersTable from '../components/ViewMembersTable'
function ViewMembers() {
  return (
    <div>
      <Navbar />
      <div class="viewmembers">
        <div class="viewmemberstable">
        <ViewMembersTable/>
        </div>
        
      </div>
    </div>
  );
}

export default ViewMembers;
