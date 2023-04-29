// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from tutorial_interfaces:msg/Encoder.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__ENCODER__FUNCTIONS_H_
#define TUTORIAL_INTERFACES__MSG__DETAIL__ENCODER__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "tutorial_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "tutorial_interfaces/msg/detail/encoder__struct.h"

/// Initialize msg/Encoder message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * tutorial_interfaces__msg__Encoder
 * )) before or use
 * tutorial_interfaces__msg__Encoder__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
bool
tutorial_interfaces__msg__Encoder__init(tutorial_interfaces__msg__Encoder * msg);

/// Finalize msg/Encoder message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
void
tutorial_interfaces__msg__Encoder__fini(tutorial_interfaces__msg__Encoder * msg);

/// Create msg/Encoder message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * tutorial_interfaces__msg__Encoder__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
tutorial_interfaces__msg__Encoder *
tutorial_interfaces__msg__Encoder__create();

/// Destroy msg/Encoder message.
/**
 * It calls
 * tutorial_interfaces__msg__Encoder__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
void
tutorial_interfaces__msg__Encoder__destroy(tutorial_interfaces__msg__Encoder * msg);

/// Check for msg/Encoder message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
bool
tutorial_interfaces__msg__Encoder__are_equal(const tutorial_interfaces__msg__Encoder * lhs, const tutorial_interfaces__msg__Encoder * rhs);

/// Copy a msg/Encoder message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
bool
tutorial_interfaces__msg__Encoder__copy(
  const tutorial_interfaces__msg__Encoder * input,
  tutorial_interfaces__msg__Encoder * output);

/// Initialize array of msg/Encoder messages.
/**
 * It allocates the memory for the number of elements and calls
 * tutorial_interfaces__msg__Encoder__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
bool
tutorial_interfaces__msg__Encoder__Sequence__init(tutorial_interfaces__msg__Encoder__Sequence * array, size_t size);

/// Finalize array of msg/Encoder messages.
/**
 * It calls
 * tutorial_interfaces__msg__Encoder__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
void
tutorial_interfaces__msg__Encoder__Sequence__fini(tutorial_interfaces__msg__Encoder__Sequence * array);

/// Create array of msg/Encoder messages.
/**
 * It allocates the memory for the array and calls
 * tutorial_interfaces__msg__Encoder__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
tutorial_interfaces__msg__Encoder__Sequence *
tutorial_interfaces__msg__Encoder__Sequence__create(size_t size);

/// Destroy array of msg/Encoder messages.
/**
 * It calls
 * tutorial_interfaces__msg__Encoder__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
void
tutorial_interfaces__msg__Encoder__Sequence__destroy(tutorial_interfaces__msg__Encoder__Sequence * array);

/// Check for msg/Encoder message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
bool
tutorial_interfaces__msg__Encoder__Sequence__are_equal(const tutorial_interfaces__msg__Encoder__Sequence * lhs, const tutorial_interfaces__msg__Encoder__Sequence * rhs);

/// Copy an array of msg/Encoder messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_tutorial_interfaces
bool
tutorial_interfaces__msg__Encoder__Sequence__copy(
  const tutorial_interfaces__msg__Encoder__Sequence * input,
  tutorial_interfaces__msg__Encoder__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__ENCODER__FUNCTIONS_H_
