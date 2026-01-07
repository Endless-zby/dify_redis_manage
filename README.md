# Redis Manage Plugin

**Author:** byzhao  
**Version:** 0.0.3  
**Type:** tool  

[English](README.md) | [中文](README_CN.md)

## Description

A comprehensive Redis management plugin for Dify that provides extensive operations across multiple Redis data structures. This plugin enables seamless integration with Redis databases, offering a wide range of operations for efficient data management within Dify workflows.

![APIKEY授权配置截图](_assets/img_3.png)  
![ACTIONS](_assets/img_1.png)  
![ACTIONS](_assets/img_2.png)  

## Features

- **Multi-Data Structure Support**: Comprehensive operations for String, List, and Geospatial data types
- **Secure Connection**: Configurable Redis connection with authentication support
- **Flexible Configuration**: Support for multiple Redis databases with customizable host, port, and authentication
- **Dify Integration**: Seamless integration with Dify's AI workflows and tools

## Configuration

The plugin requires the following credentials for Redis connection:

- **REDIS_HOST**: Redis server hostname or IP address
- **REDIS_PORT**: Redis server port (default: 6379)
- **REDIS_DB**: Redis database selection (0-15)
- **REDIS_PASSWORD**: Redis server password (optional, if authentication is required)

## Tools

This Redis plugin provides a comprehensive suite of tools organized by Redis data structures:

### String Operations

String data type operations for key-value storage and manipulation:

- **redis_string_set**: Set a key-value pair in Redis with optional expiration time
- **redis_string_get**: Retrieve the value of a specified key from Redis
- **redis_string_incr**: Increment the numeric value of a key by one
- **redis_string_decr**: Decrement the numeric value of a key by one
- **redis_string_append**: Append a value to an existing string key
- **redis_string_strlen**: Get the length of the value stored at a key
- **redis_string_expire**: Set an expiration time (TTL) for a key
- **redis_string_ttl**: Get the remaining time-to-live for a key

### List Operations

List data type operations for ordered collections of values:

- **redis_list_get**: Retrieve elements from a list within a specified range
- **redis_list_lpush**: Insert one or more values at the head of a list
- **redis_list_rpush**: Insert one or more values at the tail of a list
- **redis_list_lpop**: Remove and return the first element of a list
- **redis_list_rpop**: Remove and return the last element of a list
- **redis_list_lindex**: Get an element from a list by its index
- **redis_list_llen**: Get the length of a list
- **redis_list_lrem**: Remove elements from a list that match a specified value
- **redis_list_ltrim**: Trim a list to a specified range

### Geospatial Operations

Geospatial data type operations for location-based data:

- **redis_geo_add**: Add geospatial items (longitude, latitude, member) to a key
- **redis_geo_dist**: Calculate the distance between two geospatial members
- **redis_geo_hash**: Get the Geohash representation of one or more members
- **redis_geo_pos**: Get the longitude and latitude of geospatial members
- **redis_geo_radius**: Find members within a specified radius from a coordinate
- **redis_geo_radius_by_member**: Find members within a radius from a member's location
- **redis_geo_rem**: Remove geospatial members from a key

## Architecture & Design

This plugin follows Dify's plugin architecture standards:

- **Modular Design**: Each Redis operation is implemented as a separate tool
- **Common Utilities**: Shared Redis client functionality in `utils/redis_client.py`
- **Configuration Management**: Centralized tool configuration in provider YAML files
- **Error Handling**: Comprehensive error handling and validation across all operations

## Supported Redis Data Types

The plugin currently supports the following Redis data types:

- **String**: Basic key-value operations with TTL support
- **List**: Ordered collection operations with push/pop functionality
- **Geospatial**: Location-based operations with radius queries

*Note: Future versions will include support for Hash, Set, and Sorted Set data types.*

## Use Cases

- **Caching Solutions**: Implement caching layers within Dify workflows
- **Session Management**: Store and manage user session data
- **Geolocation Services**: Handle location-based queries and operations
- **Real-time Data Processing**: Process and store real-time data streams
- **Task Queues**: Implement queue-based task management systems

## Technical Specifications

- **Runtime**: Python 3.12
- **Required Dependencies**: See [requirements.txt](requirements.txt)

## Security Considerations

- All Redis connections support password authentication
- Credentials are securely managed through Dify's credential system
- Network communication follows Redis security best practices

## Future Enhancements

- **Hash Operations**: Add support for Redis Hash data type operations
- **Set Operations**: Implement Redis Set data type operations
- **Sorted Set Operations**: Add Redis Sorted Set (ZSet) operations
- **Advanced Features**: Add Pub/Sub, Transactions, and Pipeline operations