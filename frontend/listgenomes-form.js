

{
    "$type": "Form",
    "fields": [
        {
            "$type": "TextBox",
            "size": 400,
            "minLength": 0,
            "maxLength": 150,
            "value": "Example [LocalDateTime]",
            "label": "Analysis Name",
            "required": true,
            "requiredMessage": "Please enter name for your app session.",
            "id": "app-session-name"
        },
/*
        {
            "$type": "SampleChooser",
            "size": 300,
            "valueType": "Input",
            "allowedPermissions": "read",
            "label": "Sample",
            "required": false,
            "id": "sample-id",
            "rules": "sample-reader"
        },
*/
        {
            "$type": "ProjectChooser",
            "size": 300,
            "valueType": "Output",
            "allowedPermissions": "owner",
            "label": "Save Results To",
            "required": true,
            "requiredMessage": "Please choose a project",
            "id": "project-id",
            "allowResourceCreation": true,
            "rules": "is-project-owner"
        },
        {
            "$type": "SectionBreak"
        }
    ],
    "rulesets":[
/*
        {
            "$type": "PermissionValidationRule",
            "permissions": "Read",
            "severity": "Error",
            "message": "You do not have read access to the selected sample",
            "id": "sample-reader"
        },
*/
        {
            "$type": "PermissionValidationRule",
            "permissions": "Own",
            "severity": "Error",
            "message": "You aren't the owner of the selected project.",
            "id": "is-project-owner"
        }
    ]
}