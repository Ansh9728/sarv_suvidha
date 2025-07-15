from pydantic import BaseModel, Field
from typing import Optional, List


class BogieDetails(BaseModel):
    """ BogieDetails."""
    bogieNo: str
    makerYearBuilt: str
    incomingDivAndDate: str
    deficitComponents: str
    dateOfIOH: str
    
    
class BogieChecksheet(BaseModel):
    """ BogieChecksheet."""
    
    bogieFrameCondition: str
    bolster: str
    bolsterSuspensionBracket: str
    lowerSpringSeat: str
    axleGuide: str


class BmbcChecksheet(BaseModel):
    """ BmbcChecksheet."""
    cylinderBody: str
    pistonTrunnion: str
    adjustingTube: str
    plungerSpring: str

class BogieFormCreate(BaseModel):
    
    """ BogieFormCreate."""
    
    formNumber: str
    inspectionBy: str
    inspectionDate: str
    bogieDetails: BogieDetails
    bogieChecksheet: BogieChecksheet
    bmbcChecksheet: BmbcChecksheet
    
    
# wheell specification schema

class WheelSpecFields(BaseModel):
    condemningDia: str
    lastShopIssueSize: str
    treadDiameterNew: str
    wheelGauge: str

class WheelSpecResponseItem(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str  # consistency with query param
    fields: WheelSpecFields

class WheelSpecResponse(BaseModel):
    data: List[WheelSpecResponseItem]
    message: str
    success: bool