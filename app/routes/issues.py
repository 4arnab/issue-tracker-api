import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, IssueOut, IssueUpdate # app models <like dtos>
from app.storage import load_data, save_data

router = APIRouter(prefix="/api/v1/issues", tags=['issues'])

@router.get("/", response_model=list[IssueOut]) # list of IssueOut
def read_issues():
    """ Read all issues """
    issues = load_data()
    return issues


@router.post("/", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
def create_issue(issue:IssueCreate):
    issues = load_data()
    new_id = str(uuid.uuid4())

    new_issue = {
        "id": new_id,
        "title": issue.title,
        "description": issue.description,
        "status":issue.status,
        "priority":issue.priority,
    }

    issues.append(new_issue)
    save_data(issues)
    return new_issue

@router.get("/{issue_id}", response_model=IssueOut)
def read_issue(issue_id:str):
    issues =load_data()

    for issue in issues:
        if issue['id'] == issue_id:
            return issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

@router.put("/{issue_id}", response_model=IssueOut)
def update_issue(issue_id:str, issue:IssueUpdate):
    issues = load_data();

    for i, existing_issue in enumerate(issues):
        if existing_issue['id'] == issue_id:
            # update data 
            existing_issue['title'] = issue.title or existing_issue['title']
            existing_issue['description'] = issue.description or existing_issue['description']
            existing_issue['status'] = issue.status or existing_issue['status']
            existing_issue['priority'] = issue.priority or existing_issue['priority']

            issues[i] = existing_issue
            save_data(issues)
            return existing_issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_issue(issue_id:str):
    issues = load_data()

    for i, existing_issue in enumerate(issues):
        if existing_issue['id'] == issue_id:
            issues.pop(i)
            save_data(issues)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")