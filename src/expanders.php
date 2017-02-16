<?php

namespace Yay\DSL\Expanders;

use Yay\Token;
use Yay\TokenStream;

function class_accessors_return($stream): TokenStream
{
    if (!empty($stream->current())) {
        $stream = ": {$stream}";
    }

    return TokenStream::fromSequence(
        new Token(T_CONSTANT_ENCAPSED_STRING, $stream)
    );
}
