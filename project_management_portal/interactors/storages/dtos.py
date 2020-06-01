from dataclasses import dataclass
from project_management_portal.constants.enums import ProjectType
from typing import List, Optional
from datetime import datetime


@dataclass
class UserAdminDto:
    name: str
    username: str
    is_admin: bool


@dataclass
class WorkflowTypeDto:
    name: str
    workflow_type_id: int


@dataclass
class UserDto:
    name: str
    user_id: str
    profile_pic: str
    is_admin: bool


@dataclass
class ProjectDto:
    user_id: int
    project_id: int
    name: str
    description: str
    workflow_type: WorkflowTypeDto
    project_type: ProjectType
    created_by: UserDto
    created_at: datetime

@dataclass
class TaskDto:
    title: str
    task_id: int
    description: str
    state_id: int
    issue_type: str
    assigned_to: UserDto
    project_id: int

@dataclass
class ProjectDetailsDto:
    user_dto: UserDto
    project_dto: ProjectDto
    workflow_type_dto: WorkflowTypeDto


@dataclass
class ListOfProjectsDto:
    projects_dto: List[ProjectDto]

@dataclass
class ListOfTaskssDto:
    tasks_dto: List[TaskDto]