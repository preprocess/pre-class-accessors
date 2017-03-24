<?php

namespace Yay\DSL\Expanders;

use Yay\Engine;
use Yay\Token;
use Yay\TokenStream;

function class_accessors_return($stream, Engine $engine): TokenStream
{
    if (!empty($stream->current())) {
        $stream = ": {$stream}";
    }

    return TokenStream::fromSource(
        $engine->expand($stream, '', Engine::GC_ENGINE_DISABLED)
    );
}
