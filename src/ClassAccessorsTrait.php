<?php

namespace Pre\ClassAccessors;

trait ClassAccessorsTrait
{
    /**
     * @inheritdoc
     *
     * @param string $property
     * @param mixed $value
     */
    public function __get($property)
    {
        return $this->__class_accessor_get($property);
    }

    /**
     * @param string $property
     * @param mixed $value
     */
    protected function __class_accessor_get($property)
    {
        if (method_exists($this, "__class_accessor_get_{$property}")) {
            return $this->{"__class_accessor_get_{$property}"}();
        }

        return $this->__class_accessor_get_fallback($property);
    }

    /**
     * @inheritdoc
     *
     * @param string $property
     * @param mixed $value
     */
    public function __set($property, $value)
    {
        return $this->__class_accessor_set($property, $value);
    }

    /**
     * @param string $property
     * @param mixed $value
     */
    protected function __class_accessor_set($property, $value)
    {
        if (method_exists($this, "__class_accessor_set_{$property}")) {
            return $this->{"__class_accessor_set_{$property}"}($value);
        }

        return $this->__class_accessor_set_fallback($property, $value);
    }

    /**
     * @inheritdoc
     *
     * @param string $property
     */
    public function __unset($property)
    {
        return $this->__class_accessor_unset($property);
    }

    /**
     * @param string $property
     */
    protected function __class_accessor_unset($property)
    {
        if (method_exists($this, "__class_accessor_unset_{$property}")) {
            return $this->{"__class_accessor_unset_{$property}"}();
        }

        return $this->__class_accessor_unset_fallback($property);
    }
}
