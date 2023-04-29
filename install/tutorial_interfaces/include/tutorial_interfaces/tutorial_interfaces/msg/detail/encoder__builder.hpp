// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from tutorial_interfaces:msg/Encoder.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__ENCODER__BUILDER_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__ENCODER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "tutorial_interfaces/msg/detail/encoder__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace tutorial_interfaces
{

namespace msg
{

namespace builder
{

class Init_Encoder_second
{
public:
  explicit Init_Encoder_second(::tutorial_interfaces::msg::Encoder & msg)
  : msg_(msg)
  {}
  ::tutorial_interfaces::msg::Encoder second(::tutorial_interfaces::msg::Encoder::_second_type arg)
  {
    msg_.second = std::move(arg);
    return std::move(msg_);
  }

private:
  ::tutorial_interfaces::msg::Encoder msg_;
};

class Init_Encoder_first
{
public:
  Init_Encoder_first()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Encoder_second first(::tutorial_interfaces::msg::Encoder::_first_type arg)
  {
    msg_.first = std::move(arg);
    return Init_Encoder_second(msg_);
  }

private:
  ::tutorial_interfaces::msg::Encoder msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::msg::Encoder>()
{
  return tutorial_interfaces::msg::builder::Init_Encoder_first();
}

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__ENCODER__BUILDER_HPP_
