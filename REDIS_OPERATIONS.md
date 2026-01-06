# Redis 数据结构常用操作指南

Redis 支持多种数据结构，每种都有其特定的操作命令。本文档总结了 String、Hash、List、Set、Sorted Set/ZSet 和 Geospatial 等数据结构的常用操作。

## 1. String（字符串）

字符串是 Redis 最基本的数据类型，可以存储文本、数字或二进制数据。

### 常用操作命令：

| 命令 | 描述 | 示例 |
|------|------|------|
| SET key value | 设置指定 key 的值 | SET name "John" |
| GET key | 获取指定 key 的值 | GET name |
| GETSET key value | 设置值并返回旧值 | GETSET name "Jane" |
| SETEX key seconds value | 设置带过期时间的值 | SETEX session 3600 "token" |
| SETNX key value | 只有当 key 不存在时才设置值 | SETNX lock "locked" |
| INCR key | 将 key 存储的数字值加一 | INCR counter |
| INCRBY key increment | 将 key 存储的数字值增加指定量 | INCRBY counter 5 |
| DECR key | 将 key 存储的数字值减一 | DECR counter |
| DECRBY key decrement | 将 key 存储的数字值减少指定量 | DECRBY counter 3 |
| APPEND key value | 将值追加到已存在的字符串 | APPEND message " world" |
| STRLEN key | 获取存储在 key 中的值的长度 | STRLEN name |
| MGET key1 [key2...] | 获取所有给定 key 的值 | MGET name age |
| MSET key1 value1 [key2 value2...] | 同时设置多个 key-value 对 | MSET name "John" age 30 |

## 2. Hash（哈希）

哈希是一个键值对集合，适合存储对象。

### 常用操作命令：

| 命令 | 描述 | 示例 |
|------|------|------|
| HSET key field value | 设置哈希表 key 中的字段值 | HSET user:1 name "John" |
| HGET key field | 获取哈希表中指定字段的值 | HGET user:1 name |
| HMSET key field1 value1 [field2 value2...] | 同时设置哈希表中多个字段值 | HMSET user:1 name "John" age 30 |
| HMGET key field1 [field2...] | 获取哈希表中一个或多个字段的值 | HMGET user:1 name age |
| HGETALL key | 获取哈希表中所有的字段和值 | HGETALL user:1 |
| HDEL key field1 [field2...] | 删除哈希表中一个或多个字段 | HDEL user:1 name |
| HLEN key | 获取哈希表中字段的数量 | HLEN user:1 |
| HEXISTS key field | 查看哈希表中指定字段是否存在 | HEXISTS user:1 name |
| HKEYS key | 获取哈希表中所有的字段名 | HKEYS user:1 |
| HVALS key | 获取哈希表中所有的值 | HVALS user:1 |
| HINCRBY key field increment | 为哈希表中的字段值加上指定增量 | HINCRBY user:1 age 1 |
| HSTRLEN key field | 返回哈希表中指定字段值的字符串长度 | HSTRLEN user:1 name |

## 3. List（列表）

列表是简单的字符串列表，按照插入顺序排序。

### 常用操作命令：

| 命令 | 描述 | 示例 |
|------|------|------|
| LPUSH key value1 [value2...] | 将一个或多个值插入到列表头部 | LPUSH mylist "item1" |
| RPUSH key value1 [value2...] | 将一个或多个值插入到列表尾部 | RPUSH mylist "item2" |
| LPOP key | 移除并返回列表的第一个元素 | LPOP mylist |
| RPOP key | 移除并返回列表的最后一个元素 | RPOP mylist |
| LRANGE key start stop | 获取列表中指定范围内的元素 | LRANGE mylist 0 -1 |
| LINDEX key index | 通过索引获取列表中的元素 | LINDEX mylist 0 |
| LLEN key | 获取列表长度 | LLEN mylist |
| LREM key count value | 移除列表中与指定值相等的元素 | LREM mylist 2 "item" |
| LSET key index value | 通过索引设置列表元素的值 | LSET mylist 0 "new_item" |
| LTRIM key start stop | 对列表进行修剪，只保留指定区间内的元素 | LTRIM mylist 0 100 |
| LINSERT key BEFORE\|AFTER pivot value | 在列表的元素前或后插入元素 | LINSERT mylist BEFORE "item1" "new" |
| RPOPLPUSH source destination | 移除列表的最后一个元素，并将其添加到另一个列表开头 | RPOPLPUSH list1 list2 |

## 4. Set（集合）

集合是字符串类型的无序集合，成员是唯一的。

### 常用操作命令：

| 命令 | 描述 | 示例 |
|------|------|------|
| SADD key member1 [member2...] | 向集合添加一个或多个成员 | SADD myset "item1" |
| SMEMBERS key | 返回集合中的所有成员 | SMEMBERS myset |
| SISMEMBER key member | 判断成员是否是集合的成员 | SISMEMBER myset "item1" |
| SREM key member1 [member2...] | 移除集合中一个或多个成员 | SREM SADD myset "item1" |
| SPOP key [count] | 移除并返回集合中的一个或多个随机元素 | SPOP myset |
| SRANDMEMBER key [count] | 返回集合中一个或多个随机数 | SRANDMEMBER myset 2 |
| SCARD key | 获取集合的成员数 | SCARD myset |
| SMOVE source destination member | 将成员从 source 集合移动到 destination 集合 | SMOVE set1 set2 "item" |
| SDIFF key1 [key2...] | 返回第一个集合与其他集合之间的差集 | SDIFF set1 set2 |
| SINTER key1 [key2...] | 返回多个集合的交集 | SINTER set1 set2 |
| SUNION key1 [key2...] | 返回多个集合的并集 | SUNION set1 set2 |
| SDIFFSTORE destination key1 [key2...] | 将差集存储在 destination 集合中 | SDIFFSTORE diff set1 set2 |
| SINTERSTORE destination key1 [key2...] | 将交集存储在 destination 集合中 | SINTERSTORE inter set1 set2 |
| SUNIONSTORE destination key1 [key2...] | 将并集存储在 destination 集合中 | SUNIONSTORE union set1 set2 |

## 5. Sorted Set / ZSet（有序集合）

有序集合和集合一样也是字符串的集合，且不允许重复成员，但每个成员都会关联一个分数用于排序。

### 常用操作命令：

| 命令 | 描述 | 示例 |
|------|------|------|
| ZADD key score1 member1 [score2 member2...] | 向有序集合添加一个或多个成员 | ZADD leaderboard 100 "player1" |
| ZRANGE key start stop [WITHSCORES] | 通过索引区间返回有序集合指定区间内的成员 | ZRANGE leaderboard 0 -1 WITHSCORES |
| ZREVRANGE key start stop [WITHSCORES] | 返回有序集中指定区间内的成员（分数从高到低） | ZREVRANGE leaderboard 0 -1 WITHSCORES |
| ZREM key member [member...] | 移除有序集合中的一个或多个成员 | ZREM leaderboard "player1" |
| ZCARD key | 获取有序集合的成员数 | ZCARD leaderboard |
| ZSCORE key member | 返回有序集中指定成员的分数 | ZSCORE leaderboard "player1" |
| ZRANK key member | 返回有序集合中指定成员的排名（从小到大） | ZRANK leaderboard "player1" |
| ZREVRANK key member | 返回有序集合中指定成员的排名（从大到小） | ZREVRANK leaderboard "player1" |
| ZINCRBY key increment member | 有序集合中成员的分数加上增量 | ZINCRBY leaderboard 10 "player1" |
| ZCOUNT key min max | 计算在有序集合中指定区间分数的成员数 | ZCOUNT leaderboard 90 100 |
| ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count] | 通过分数返回有序集合指定区间内的成员 | ZRANGEBYSCORE leaderboard 90 100 WITHSCORES |
| ZREMRANGEBYRANK key start stop | 移除有序集合中给定排名区间的所有成员 | ZREMRANGEBYRANK leaderboard 0 1 |
| ZREMRANGEBYSCORE key min max | 移除有序集合中给定分数区间的所有成员 | ZREMRANGEBYSCORE leaderboard 0 50 |
| ZUNIONSTORE destination numkeys key [key...] | 计算给定的一个或多个有序集的并集 | ZUNIONSTORE result 2 set1 set2 |
| ZINTERSTORE destination numkeys key [key...] | 计算给定的一个或多个有序集的交集 | ZINTERSTORE result 2 set1 set2 |

## 6. Geospatial（地理空间）

Redis 的地理空间功能允许存储地理位置信息，并执行距离计算和位置查询等操作。

### 常用操作命令：

| 命令 | 描述 | 示例 |
|------|------|------|
| GEOADD key longitude latitude member [longitude latitude member...] | 添加地理位置信息 | GEOADD cities 13.361389 38.115556 "Palermo" |
| GEOPOS key member [member...] | 获取地理位置信息 | GEOPOS cities "Palermo" |
| GEODIST key member1 member2 [unit] | 计算两个位置之间的距离 | GEODIST cities "Palermo" "Catania" km |
| GEORADIUS key longitude latitude radius m\|km\|ft\|mi [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count] | 以给定坐标为中心查找指定范围内的位置 | GEORADIUS cities 15 37 200 km |
| GEORADIUSBYMEMBER key member radius m\|km\|ft\|mi [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count] | 以给定位置为中心查找指定范围内的位置 | GEORADIUSBYMEMBER cities "Palermo" 200 km |
| GEOHASH key member [member...] | 获取位置的 Geohash 表示 | GEOHASH cities "Palermo" |
| ZREM key member [member...] | 移除地理位置信息（使用有序集命令） | ZREM cities "Palermo" |

## 总结

以上就是 Redis 中常用的六种数据结构及其主要操作命令。掌握这些命令可以帮助您更有效地使用 Redis 进行开发工作。不同的数据结构适用于不同的场景，选择合适的数据结构对于系统性能至关重要。