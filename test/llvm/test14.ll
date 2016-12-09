; ModuleID = '../src/test14.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test14() #0 {
  %local1 = alloca i32, align 4
  store i32 0, i32* %local1, align 4
  %1 = load i32, i32* %local1, align 4
  %2 = add nsw i32 %1, 2
  store i32 %2, i32* %local1, align 4
  br label %3

; <label>:3                                       ; preds = %0
  %4 = load i32, i32* %local1, align 4
  ret i32 %4
}

attributes #0 = { nounwind "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-features"="+mmx,+sse,+sse2" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.8.0-2ubuntu4 (tags/RELEASE_380/final)"}
