<?php

namespace Pre;

trait AccessorsTrait
{
    /**
     * @inheritdoc
     *
     * @param string $property
     * @param mixed $value
     */
    public function __get($property)
    {
        if (method_exists($this, "__get_{$property}")) {
            return $this->{"__get_{$property}"}();
        }
    }

    /**
     * @inheritdoc
     *
     * @param string $property
     * @param mixed $value
     */
    public function __set($property, $value)
    {
        if (method_exists($this, "__set_{$property}")) {
            return $this->{"__set_{$property}"}($value);
        }
    }
}
