## Design Uber

Uber is a ride-sharing platforms that connect passengers with drivers who offer transportation services in personal vehicles. It allows users to book rides on-demand from their smartphones, matching them with a nearby driver who will take them from their location to their desired destination.

![Uber Design Diagram](../assets/uber/uber.png)

## Functional Requirements

1. Users should be able to input a start location and a destination and get an estimated fare.
2. User should be able to request a ride based on an estimate
3. Drivers should be able to accept/deny a request and navigate to pickup/dropoff.

--- Out of Scope ---

- Multiple car types
- Rating for drivers and riders
- Schedule a ride in advance

### Non-functional requirements

- Low latency matching < 1 min to match or failure
- Consistency of matching, Ride to driver is 1:1
- Highly available outside the matching
- Handle high throughput, sruges for peak hours or special events, 100s of thousands of requests withing a given region

--- Out of Scope ---

- GDPR user privacy
- Resilienc and handling system failure
- Monitoring, logging, alerting etc..
- CI/CD pipeline

## Core Entities

- Ride
- Driver
- Rider
- Location

### API

```
POST /ride/fare-estimate -> Partial<Ride>
{
	source,
	destination
}
```

```
PATCH /ride/request -> 200
{
	rideId
}
```

```
POST /location/update
{
	lat,
	long
}
```

```
PATCH /ride/driver/accept
{
	rideId,
	true/false
}
```

```
PATCH /ride/driver/update
{
	rideId,
	status: 'pickup' | 'dropoff'
}
```

## High Level Design

![High Level Design](../assets/uber/HighLevel.png)

## QuadTrees (PostGIS)

- Choose this when the distribution is uneven or uneven density and also when theres no high frequency of updates.

![QuadTrees](../assets/uber/QuadTrees.png)

## Geohashing (Redis)

- Indiscriminate in-terms of density, the world is split into evenly precise boxes
- Really god for high frequency of updates

![Geohashing](../assets/uber/Geohasing.png)

## Note

Uber uses H3: Uber’s Hexagonal Hierarchical Spatial Index.

Read more: https://www.uber.com/en-IN/blog/h3/

Github: https://github.com/uber/h3
