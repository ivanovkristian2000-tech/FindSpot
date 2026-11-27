# FindSpot — Development Roadmap

## Project description

FindSpot is a backend application for a housing rental platform built with Django, Django REST Framework and MySQL.

## Stage 1 — Project Setup

- [x] FS-001 — Initialize Django project
- [x] FS-002 — Create virtual environment
- [x] FS-003 — Create GitHub repository
- [x] FS-004 — Configure remote repository
- [x] FS-005 — Configure .gitignore
- [x] FS-006 — Configure environment variables
- [x] FS-007 — Initial commit and push
- [x] FS-008 — Create and register Django applications
- [x] FS-009 — Install initial dependencies
- [x] FS-010 — Verify Django configuration and startup
- [x] FS-011 — Create project roadmap

## Stage 2 — Users and Authentication

- [ ] Design database models and relationships
- [x] Create custom user model
- [ ] Configure renter and landlord groups and permissions
- [x] Configure MySQL database
- [x] Configure SQLite for local development
- [x] Create and apply migrations
- [ ] Implement user registration
- [ ] Implement login and logout
- [ ] Configure authentication
- [ ] Implement role-based permissions
- [ ] Test authentication and permissions

## Stage 3 — Listings

- [x] Create listing model
- [ ] Implement listing creation
- [ ] Implement listing retrieval
- [ ] Implement listing updates
- [ ] Implement listing deletion
- [ ] Implement active and inactive statuses
- [ ] Implement ownership permissions
- [ ] Test listing endpoints

## Stage 4 — Search and Filtering

- [ ] Search by title and description
- [ ] Filter by price range
- [ ] Filter by location
- [ ] Filter by number of rooms
- [ ] Filter by property type
- [ ] Sort by price
- [ ] Sort by creation date
- [ ] Implement pagination
- [ ] Test search and filtering

## Stage 5 — Reservations

- [x] Create reservation model
- [ ] Implement reservation creation
- [ ] Validate reservation dates
- [ ] Prevent overlapping reservations
- [ ] Retrieve active and completed reservations
- [ ] Implement reservation confirmation
- [ ] Implement reservation rejection
- [ ] Implement reservation cancellation
- [ ] Validate status transitions and permissions
- [ ] Test reservation business logic

## Stage 6 — Reviews and Ratings

- [x] Create review model
- [ ] Implement ratings and reviews
- [ ] Retrieve listing reviews
- [ ] Validate completed reservations before reviewing
- [ ] Test review functionality

## Stage 7 — Docker and Deployment

- [ ] Create Dockerfile
- [ ] Configure Docker Compose
- [ ] Configure Django and MySQL containers
- [ ] Prepare .env.example
- [ ] Test containerized application
- [ ] Deploy application to AWS EC2

## Stage 8 — Testing and Final Presentation

- [ ] Review project architecture
- [ ] Review validation and error handling
- [ ] Test all API endpoints
- [ ] Fix discovered bugs
- [ ] Verify all project requirements
- [ ] Update requirements.txt
- [ ] Create README.md
- [ ] Document installation and deployment
- [ ] Prepare project presentation
- [ ] Practice technical interview questions
- [ ] Submit final project

## Optional Features

- [ ] Search history
- [ ] Popular search queries
- [ ] Listing view history
- [ ] Popularity-based sorting
