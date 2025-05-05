# ColabDev: University Open Day Management System API

## Project Overview

ColabDev is a collaborative development project created as part of the 5CS024/UM1: Collaborative Development module at the University of Wolverhampton. This project demonstrates the practical application of software development in a team environment, focusing on security-by-design principles and business-driven development.

### Academic Context
- **Module**: 5CS024/UM1: Collaborative Development
- **Institution**: University of Wolverhampton (City Campus)
- **Level**: Undergraduate Level 5

### Project Objectives
- Demonstrate collaborative software development in a team environment
- Implement security-by-design principles
- Create a business-focused solution for university open day management
- Apply modern software development methodologies

## Technical Overview

### Security Features
- JWT-based authentication system
- SQL injection prevention through ORM
- Secure password hashing
- HTTPS encryption support
- Input validation and sanitization
- Rate limiting protection

### Business Value
- Streamlines university open day management
- Reduces administrative overhead
- Improves participant experience
- Provides data-driven insights
- Supports marketing and recruitment efforts

## API Documentation

### Base URL
```
https://colabdev-api.azurewebsites.net/api
```

### Database Configuration
- **Type**: Azure Database for PostgreSQL
- **Tier**: General Purpose
- **Storage**: 32GB
- **Backup**: Automated daily backups with 7-day retention
- **High Availability**: Zone-redundant configuration
- **Monitoring**: Azure Monitor integration
- **Security**: Private endpoint enabled, SSL enforced
- **Performance**: Query performance insights enabled
- **Scaling**: Auto-scaling configured for peak loads

### Authentication

The API implements secure JWT (JSON Web Token) authentication, following security-by-design principles:
- Tokens are encrypted and time-limited
- Password requirements enforce strong security
- Rate limiting prevents brute force attacks

To obtain a token:
1. Send a POST request to `/auth/login`
2. Include the token in subsequent requests:
```
Authorization: Bearer <your_token>
```

### Endpoints

#### Authentication

##### Login
- **POST** `/auth/login`
- **Security**: Rate limited, HTTPS required
- **Description**: Authenticate user and receive access token
- **Body**:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```
- **Response**: Returns JWT token and user details

##### Register
- **POST** `/auth/register`
- **Security**: Rate limited, password strength validation
- **Description**: Register a new user
- **Body**:
```json
{
    "fullname": "Test User",
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123"
}
```

#### Events

##### Get All Events
- **GET** `/events`
- **Security**: Public endpoint with rate limiting
- **Description**: Retrieve all events
- **Business Impact**: Provides prospective students with event information
- **Query Parameters**:
  - `group_by=date` (optional): Group events by date

##### Create Event
- **POST** `/events`
- **Security**: Authenticated, admin-only
- **Description**: Create a new event
- **Business Impact**: Enables staff to manage open day schedule
- **Body**:
```json
{
    "title": "New Event",
    "description": "Event description",
    "date": "2024-04-01",
    "time": "14:00",
    "duration": "2 hours",
    "location": "Main Campus",
    "public": true
}
```

#### Registrations

##### Create Registration
- **POST** `/registration`
- **Security**: Public endpoint with enhanced validation
- **Description**: Register for an open day
- **Business Impact**: Captures prospective student information
- **Data Protection**: Complies with GDPR requirements
- **Body**:
```json
{
    "title": "Mr",
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "2000-01-01",
    "email": "john@example.com",
    "phone_number": "+44123456789",
    "level_of_study": "Undergraduate",
    "subject_area": "Computer Science",
    "event_date": "2024-04-01",
    "guest_count": 2
}
```

## Security Implementation

### Data Protection
- All sensitive data is encrypted at rest
- Personal information is handled according to GDPR
- Database connections use SSL/TLS encryption
- Regular security audits and updates

### Rate Limiting
- Public endpoints: 100 requests per minute
- Authentication endpoints: 10 attempts per minute
- Protected endpoints: 200 requests per minute per token

## Business Context

### Development Considerations
- Scalable architecture for peak registration periods
- Cost-effective cloud hosting on Azure
- Maintainable codebase following best practices
- Integration capabilities with university systems

### Economic Impact
- Reduces manual processing time
- Improves data accuracy and reporting
- Enhances student recruitment process
- Provides analytics for marketing decisions

## Technology Stack

- **Backend**: Python Flask (chosen for rapid development and maintainability)
- **Database**: PostgreSQL on Azure (ensures scalability and reliability)
- **Security**: JWT, SSL/TLS, Rate Limiting
- **Documentation**: OpenAPI/Swagger
- **Version Control**: Git
- **CI/CD**: GitHub Actions

## Development Team

This project was developed as part of the 5CS024/UM1 module by:
- **Project Manager (PM)**: Anwar Syed Ali (2359582) - Project Lead, Software Developer
- **Software Developer (SWD)**: Zubair Idris Aweda (2306535) - Software Development Lead, Database Support
- **Software Developer (SWD)**: Lahari Chunduri (2380572) - Developer, Project Management Support
- **Software Developer (SWD)**: Hassan Sohail - Developer
- **Database Administrator (DBA)**: Abiodun Olayade (2310952) - Database Management, Security Support
- **Security Analyst (SCA)**: Excel Ekwenuya (2402205) - Security Implementation, Business Analysis
- **Security Analyst (SCA)**: Solomon Omoigui (2007001) - Security Design, Development Support
- **Business Analyst (BSA)**: Grace Odubanjo (2383966) - Business Analysis, Security Support
- **Business Analyst (BSA)**: Zainab Shanhzad - Business Process Analysis
- Academic Year: 2023/24
- Supervisor: Lawrence Krukrubo

## Support and Maintenance

For technical support or queries:
- Email: A.Olayade@wlv.ac.uk
- Documentation: [Documentation URL]
- Issue Tracking: GitHub Issues

## Version History

### v2.0.0 (Current - MMP)
- Database migration from Render to Azure for improved scalability and performance
- Enhanced database management and monitoring capabilities
- Optimized database configurations for enterprise-level performance
- Implemented advanced backup and recovery procedures

### v1.0.0 (MVP)
- Initial Release with core functionality
- Database hosted on Render for rapid deployment
- Basic security features implementation
- Core API documentation

## Learning Outcomes Achieved

1. **LO1**: Demonstrated through collaborative development and timely delivery
2. **LO2**: Evidenced by business-focused features and economic considerations
3. **LO3**: Implemented through comprehensive security measures

## Future Enhancements

- Advanced analytics dashboard
- Mobile application support
- Integration with university CRM
- Enhanced reporting features 